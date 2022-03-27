from django.db import models
from django.contrib.postgres.fields import ArrayField


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    long_name = models.CharField(max_length=35)
    short_name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class Stop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    long = models.IntegerField()
    lat = models.IntegerField()
    code = models.IntegerField()
    routes = models.ManyToManyField(Route)

class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    call_name = models.CharField(max_length=20)
    long = models.IntegerField()
    lat = models.IntegerField()
    service_status = models.CharField(max_length=12)
    route_id = models.ForeignKey(Route,on_delete=models.DO_NOTHING)


from django.conf import settings
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Create your models here.

class UserSettings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False)
    start = models.IntegerField(default=5)

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['phone', 'start']
        widgets = {
                'phone': PhoneNumberPrefixWidget(attrs={'placeholder': ('Phone')}),
                'start': forms.TextInput(attrs={'type': 'range', 'min': '1', 'max': '11', 'step': '1', 'value': '6', 'list': 'tickmarks'}),
            }
