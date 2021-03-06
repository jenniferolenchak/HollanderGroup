from django.contrib import admin
from .models import Settings, BudgetList, CashFlow

# Register your models here.
admin.site.register(Settings)
admin.site.register(BudgetList)
admin.site.register(CashFlow)
