from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.dashboard_view, name = "dashboard_view"),
    path('settings/', views.settings_view, name = "settings_view"),
    path('settings/retry/', views.change_settings, name = "change_settings"),
    path('accounts/', include('allauth.urls')),
]
