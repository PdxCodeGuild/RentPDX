from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = CustomUser
        fields = [
            'username',
            'email',
            'user_type',
            'birthdate',
            'first_name',
            'last_name',          
        ]

        #this will be necessary soon 
        # fields = UserCreationForm.Meta.fields + ('user_type','first_name','last_name','birthdate')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'user_type',
            'birthdate',
            'first_name',
            'last_name',         
        ]
        #this will be necessary soon 
        # fields = UserCreationForm.Meta.fields + ('user_type','first_name','last_name','birthdate')
