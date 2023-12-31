from email.message import EmailMessage
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as LOGIN
from django.contrib.auth.decorators import login_required
from django.http import request, JsonResponse
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from users.forms import (
    PitEditForm,
    UserCreationForm,
    UserLoginForm,
    UserChangeForm,
    UserEditForm,
    ProfileEditForm,
    NameEditForm,

    ProfileSettingsForm,
    TeamSettingsForm,

    TeamEditForm
)
from users.models import CustomUser, Profile
from teams.models import Team
from django.conf import settings
from django.template import loader
from stats.models import Pit_stats, Game_stats, Match
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.http import HttpResponse
import random, string

from django.shortcuts import get_object_or_404
from itertools import chain
from django.core.mail import send_mail

def index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data["first_name"]
            Feedback.objects.filter(first_name=first_name).update(
                team_num=request.user.team_num
            )
            return redirect("home-view")
    else:
        form = FeedbackForm()
    return render(request, "users/index.html", {"form": form})

def login(request):
    form = UserLoginForm(request.POST or None)
    next_url = request.GET.get("next")
    if request.method == "POST":
        if form.is_valid():
            user_obj = form.cleaned_data.get("user_obj")
            LOGIN(request, user_obj)

            if next_url:
                return redirect(next_url)
            else:
                return redirect("home-view")

        else:
            messages.warning(request, f"Invalid Credentials")

    return render(request, "users/login.html", {"form": form})

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user_obj = form.save()        
            username = form.cleaned_data["username"]
            is_team_admin = form.cleaned_data["is_team_admin"]

            email = form.cleaned_data["email"]
            
            user = CustomUser.objects.filter(username=username)
            #! set to false after registration is finished
            user.is_active = True
            
            team_num = form.cleaned_data["team_num"]
           


            if is_team_admin:
                user.update(is_admin=True)
           

            if not Team.objects.filter(team_num=team_num).exists():

                Team.objects.create(
                    team_users=user_obj, team_num=team_num
                )

                   
            
            
            LOGIN(request, user_obj)
            return redirect("home-view")
     

        else:
            # Registration error check
            messages.warning(request, "Registration invalid. Username/Email already exists")
    context = {
        'form': form,
    }
    return render(request, "users/register.html", context)

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "users/welcome.html")
    else:
        return HttpResponse("Activation link is invalid!")

def gettingStarted(request):
    return render(request, "users/getting-started.html")

def guest(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'jtyler03@optonline.net',
    ['jtyler03@optonline.net'],
    fail_silently=False,
    )
    return render(request, "users/guest.html")

@login_required
def welcome(request):
    return render(request, "users/welcome.html")

def getAuthLevel():
    if CustomUser.is_team_admin:
        return "Team Mentor"
    else:
        return "Team Member"

@login_required
def ProfileSettings(request, id):
    instance = Profile.objects.get(user=request.user.profile.user)
    form = NameEditForm(request.POST, instance=instance)
    p_form = ProfileSettingsForm(request.POST, instance=instance)
    p_first_name = Profile.objects.get(user=request.user).first_name
    p_last_name = Profile.objects.get(user=request.user).last_name
    
    context = {
        "auth_level": getAuthLevel(),
        "form": form,
        "p_form": p_form,


        'relativeScoring': Profile.objects.get(user=request.user).relativeScoring,
        'p_fn': p_first_name,
        'p_ln': p_last_name,
    }
    if request.method == "POST":
        form = NameEditForm(request.POST, instance=instance)
        #p_form = UserSettingsForm(request.POST, instance=p_instance)
        if form.is_valid:
            form.save()
            p_form.save()
            return redirect("profile-view")
    return render(request, "users/profile-settings.html", context)

@login_required
def profile(request):
    context = {
        "user_admins": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=True),
        "users": CustomUser.objects.filter(team_num=request.user.team_num, is_team_admin=False),
        "auth_level": getAuthLevel(),
        "code": Team.objects.get(team_num=request.user.team_num).team_code,
    }
    return render(request, "users/profile.html", context)

class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
      Returns a JSON response, transforming 'context' to make the payload.
      """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
      Returns an object that will be serialized as JSON by json.dumps().
      """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

@login_required
def teamManagement(request):
    if Pit_stats.objects.filter(team_num=request.user.team_num).exists():
        context = {
            'users': CustomUser.objects.filter(team_num=request.user.team_num),
            'usersCount': CustomUser.objects.filter(team_num=request.user.team_num).count(),
            'is_incorrect': Pit_stats.objects.get(team_num=CustomUser.objects.get(username=request.user.username).team_num).is_incorrect,
            'incorrect': Pit_stats.objects.get(team_num=CustomUser.objects.get(username=request.user.username).team_num).incorrect_selection,
            
            'is_hidden': Pit_stats.objects.get(team_num=CustomUser.objects.get(username=request.user.username).team_num).is_hidden,
            'link': Pit_stats.objects.get(team_num=CustomUser.objects.get(username=request.user.username).team_num).id
        }
    else:
        context = {
            'users': CustomUser.objects.filter(team_num=request.user.team_num),
            'usersCount': CustomUser.objects.filter(team_num=request.user.team_num).count(),
            
        }
    return render(request, "users/team-manager.html", context) 

@login_required
def teamInfo(request):
    instance = Team.objects.get(team_num=request.user.team_num)
    form = TeamEditForm(request.POST or None, instance=instance)
    context = {"instance": instance, "form": form}
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request, "users/team-manager.html", context)
    return render(request, "users/team-info.html", context) 

@login_required
def teamManagementUserEdit(request, id):
    
    username = Profile.objects.get(id=id).user.username

    f_name = CustomUser.objects.get(username=username).profile.first_name
    l_name = CustomUser.objects.get(username=username).profile.last_name
    username = CustomUser.objects.get(username=username)
    email = CustomUser.objects.get(username=username).email

    p_instance = CustomUser.objects.get(username=username).profile
    form = TeamSettingsForm(request.POST or None, instance=p_instance)
    context = {
        "instance": p_instance, 
        "form": form,
        "f_name": f_name,
        "l_name": l_name,
        "username": username,
        "email": email,
        "isChecked": CustomUser.objects.get(username=username).profile.canEditStats,
        "isAdmin": CustomUser.objects.get(username=username).is_admin,
        
    }
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request, "users/team-manager-user.html", context)
    return render(request, "users/team-manager-user.html", context) 

@login_required
def changelog(request):
    return render(request, "users/changelog.html")

@login_required
def passwordUpdate(request):
    return render(request, 'users/password-change.html')

@login_required
def pitUpdate(request, stat_id):
    instance = Pit_stats.objects.get(stat_id=stat_id)
    form = PitEditForm(request.POST or None, instance=instance)
    context = {"instance": instance, "form": form}
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_incorrect = False
            instance.save()
            return render(request, "users/team-manager.html", context)

    return render(request, "users/data/pit-update.html", context)


@login_required
def accountEdit(request, id):
    instance = get_object_or_404(CustomUser, id=id)
   

    form = UserEditForm(request.POST, instance=instance)
    context = {
        "auth_level": getAuthLevel(),
        "form": form,


    }
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect("profile-view")
    
    return render(request, 'users/account-edit.html', context)

def del_user(request, id):    
    
    username = CustomUser.objects.get(id=id).username

    u = User.objects.get(username = username)
    u.delete()

    return render(request, 'users/index.html')

def issues(request):    
    
    from django.core.mail import EmailMultiAlternatives

    subject, from_email, to = 'hello', 'frcsassistant@gmail.com', 'jtyler03@optonline.net'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return render(request, 'users/issues.html')

