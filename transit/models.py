from django.db import models
from django.conf import settings
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserSettings(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    threshold_eta = models.IntegerField(default=5)

class UserSettingsForm(forms.ModelForm):
    model = UserSettings
    fields = ['author', 'phone', 'threshold_eta']
    widgets = {
            'phone': forms.TextInput(attrs={'placeholder': _('Phone')}),
            'start': forms.TextInput(attrs={'type': 'range', 'min': '1', 'max': '10'}),
        }