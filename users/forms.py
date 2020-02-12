from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = CustomUser
        fields = [
            'username',
            'email'           
        ]

        #this will be necessary soon 
        #fields = UserCreationForm.Meta.fields + ('type','first_name','last_name','birthday')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email'         
        ]
        #this will be necessary soon 
        #fields = UserCreationForm.Meta.fields + ('type','first_name','last_name','birthday')
