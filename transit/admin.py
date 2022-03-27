from django.contrib import admin
from .models import UserSettings, Route, Stop, Vehicle

# Register your models here.

admin.site.register(UserSettings)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Vehicle)
