from django import forms
from django.db import models
from django.forms import fields, widgets
from . models import User

class StudentReg(forms.ModelForm):
    class Meta:
        model= User
        fields= '__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passid'})
        }