from django.urls import path
from . import views


urlpatterns = [
	path('savingsuggestions/', views.saving_suggestions, name='savingsuggestions'),
    path('settings/', views.settings, name='settings'),
    path('', views.dashboard, name='dashboard'),
]