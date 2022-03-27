from django.db import models
from django.conf import settings
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserSettings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    start = models.IntegerField(default=5)

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['phone', 'start']
        widgets = {
                'phone': forms.TextInput(attrs={'placeholder': ('Phone')}),
                'start': forms.TextInput(attrs={'type': 'range', 'min': '1', 'max': '11', 'step': '1', 'value': '5', 'list': 'tickmarks'}),
            }