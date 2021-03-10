# Generated by Django 3.1.6 on 2021-03-09 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0029_auto_20210309_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cashflow',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashflows', to=settings.AUTH_USER_MODEL),
        ),
    ]
