from django import forms
from .models import Tweet,Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text' , 'photo']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description' , 'video_file']

class User_RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
