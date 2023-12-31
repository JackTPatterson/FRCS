from django import forms
from django.forms import ModelForm
from .models import Pit_stats, Game_stats, Match
from users.models import CustomUser

DRIVETRAIN_TYPE = [
    ('4 Wheel Skid', '4 Wheel Skid'),
    ('6 Wheel Skid', '6 Wheel Skid'),
    ('8 Wheel Skid', '8 Wheel Skid'),
    ('Treads', 'Treads'),
    ('Omni', 'Omni'),
    ('Swerve','Swerve'),
    ('Other','Other'),	
]

VISION_TYPE = [
    
 ('None', 'None'),
 ('Limelight', 'Limelight'),
 ('Raspberry Pi', 'Raspberry Pi'),
 ('Other', 'Other'),
]

GOAL_SHOT = [
 ('Lower Hub', 'Lower Hub'),
 ('Upper Hub', 'Upper Hub'),
 ('Both Lower and Upper Hub', 'Both Lower and Upper Hub'),
]

INCORRECT_CHOICES = [
    ('DriveTrain Type', 'DriveTrain Type'),
    ('Height', 'Height'),
    ('Frame Perimeter', 'Frame Perimeter'),
    ('Auto', 'Auto'),
    ('Goal Shot', 'Goal Shot'),
    ('Vision Implemented', 'Vision Implemented'),
    ('Vision Type', 'Vision Type'),
    ('Climb', 'Climb'),
    ('Custom 1', 'Custom 1'),
    ('Custom 2', 'Custom 2'),
    ('Custom 3', 'Custom 3'),
]

TRUE_FALSE = [
    ('No', 'No'),
    ('Yes', 'Yes'),
]

VISION_TRUE_FALSE = [
    ('0', 'No'),
    ('1', 'Yes'),
]

CLIMB = [
    ('None', 'None'),
    ('Lower Rung', 'Lower Rung'),
    ('Middle Rung', 'Middle Rung'),
    ('Upper Rung', 'Upper Rung'),
    ('Traversal Rung', 'Traversal Ring')
    
]

class pit_scout_form(ModelForm):
    robot_drivetrain_type = forms.CharField(widget=forms.Select(choices=DRIVETRAIN_TYPE))
    robot_goal_height = forms.CharField(widget=forms.Select(choices=GOAL_SHOT))
    robot_vision_implement = forms.CharField(widget=forms.Select(choices=VISION_TRUE_FALSE))
    robot_vision_type = forms.CharField(widget=forms.Select(choices=VISION_TYPE))
    robot_autonomous = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_climb = forms.CharField(widget=forms.Select(choices=CLIMB))

    class Meta:
        model = Pit_stats
        exclude = ['scout', 'stat_id', 'date_entered', 'incorrect_selection' ,'is_incorrect', 'is_hidden']

class pit_correct_form(ModelForm):
    
    incorrect_selection = forms.CharField(widget=forms.Select(choices=INCORRECT_CHOICES))

    class Meta:
        model = Pit_stats
        fields = ['is_incorrect']

class game_scout_form(ModelForm):
    #match_number
    left_tarmac = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_climb = forms.CharField(widget=forms.Select(choices=CLIMB))
    # robot_climb_help = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    class Meta:
        model = Match
        exclude = ['scouting_teamber', 'stat', 'scout', 'score']
        
        
