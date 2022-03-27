from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="transit/dashboard.html")),
    path('settings/', TemplateView.as_view(template_name="transit/settings.html")),
    path('accounts/', include('allauth.urls')),
]
