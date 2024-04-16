from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    email = forms.EmailField()
        
class LoginForm(AuthenticationForm):
    pass

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ('title', 'subtitle', 'category','text')