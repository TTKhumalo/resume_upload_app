from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from resume_manager.models import RESUME


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class RESUMEUploadForm(forms.ModelForm):
    class Meta:
        model = RESUME
        fields = ["excel_file"]
        widgets = {
            'excel_file': forms.FileInput(attrs={'accept': '.csv'}),
        }
