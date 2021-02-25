from django.urls import path
from . import views


urlpatterns = [
    path('upcomingpayments/', views.upcoming_payments, name='upcomingpayments'),
	path('savingsuggestions/', views.saving_suggestions, name='savingsuggestions'),
    path('settings/', views.settings, name='settings'),
    path('', views.dashboard, name='dashboard'),
]