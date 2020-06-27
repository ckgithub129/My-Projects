from django import forms
from django.contrib.auth import get_user_model
from api import models
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta(object):
		model = User
		fields = ['username', 'email', 'password1', 'password2']