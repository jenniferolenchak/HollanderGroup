from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/editcashflow/<int:id>/', views.edit_cashflow, name='editcashflow'),
    path('dashboard/settings/edit_icon_url/', views.edit_icon_url, name='edit_icon_url'),
    path('dashboard/settings/edit_accountinfo/', views.edit_accountinfo, name='edit_accountinfo'),
    path('dashboard/settings/personal_info/', views.personal_info, name='personal_info'),
    path('dashboard/editmydata/', views.edit_my_data, name='editmydata'),
    path('dashboard/upcomingpayments/', views.upcoming_payments, name='upcomingpayments'),
	path('dashboard/savingsuggestions/', views.saving_suggestions, name='savingsuggestions'),
    path('dashboard/addnewpayment/', views.addnew_cashflow, name='addnewpayment'),
    path('dashboard/settings/', views.settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/allpayments/', views.all_payments, name='allpayments'),
    path('dashboard/removecashflow/<int:id>/', views.remove_cashflow, name='removecashflow')
]