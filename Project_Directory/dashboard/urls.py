from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/editmydata/', views.edit_my_data, name='editmydata'),
    path('dashboard/upcomingpayments/', views.upcoming_payments, name='upcomingpayments'),
	path('dashboard/savingsuggestions/', views.saving_suggestions, name='savingsuggestions'),
    path('dashboard/settings/', views.settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
]