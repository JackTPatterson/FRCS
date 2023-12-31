import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import request
from teams.models import Team, Match
import string
from .models import Pit_stats
from .forms import pit_scout_form, game_scout_form
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
import tbapy
from .models import Game_stats
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
# Create your views here.

#@login_required
#def scout(request):
#  return render(request, 'stats/scout.html', {'team_num': request.user.team_num})

def scouthub(request):
  return render(request, 'stats/scout-hub.html', {'team_count': Team.objects.all().count()})

def pitdata(request):
  return render(request, 'stats/pit-data.html')

class ScoutDetailView(DetailView):
  model = Game_stats
  #return render(request, 'stats/game-data.html')

class ScoutListView(ListView):
  model = Game_stats
  template_name = 'stats/game_stats_list'  # <app>/<model>_<viewtype>.html
  context_object_name = 'teams'
  ordering = ['-id']

class PitListView(ListView):
  model = Pit_stats
  template_name = 'stats/pit_stats_list'
  context_object_name = 'teams'
  ordering = ['-id']

class PitDetailView(DetailView):
  model = Pit_stats

@login_required
def feed(request):
  return render(request, 'stats/feed.html')

#def pitdata(request):
#  return render(request, 'stats/pit-data.html')

def gamedata(request):
  return render(request, 'stats/game-data.html')

#def pitdatahub(request):
#  return render(request, 'stats/pit-data-hub.html')

#def gamedatahub(request):
#  return render(request, 'stats/game-data-hub.html', {'teams': Game_stats.objects.all()})

def test(request):
  return render(request, 'stats/test.html')

def pit_scout(request):
  form = pit_scout_form(request.POST)
  competitions = []
  if request.method == 'POST':
    if form.is_valid():
      form.save(commit=False)
      team_num = form.cleaned_data['team_num']

      if not Team.objects.filter(team_num = team_num).exists():
        Team.objects.create(team_num = team_num)

      if Pit_stats.objects.filter(team_num = team_num).exists():
        return redirect('home-view')
      form.save()
      return redirect('home-view')
    else:
      return redirect('home-view')
  return render(request, 'stats/pit-scout.html', {'form': form})

@login_required
def scout(request):
  form = game_scout_form(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      obj = form.save(commit=False)
      obj.team_num = request.user.team_num
      team_num = form.cleaned_data['scouting_team']
      match_num = form.cleaned_data['match_number']
      new_match = Match.objects.create(game_stats = obj, match_number = match_num)
      if not Team.objects.filter(team_num = team_num).exists():
        Team.objects.create(team_num = team_num)
      Team.objects.filter(team_num = team_num).update(matches = new_match)
      form.save()
      return redirect('home-view')
    else:
      return redirect('home-view')
  return render(request, 'stats/scout.html', {'form': form})

