# Generated by Django 3.1.6 on 2021-03-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_auto_20210315_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow',
            name='day',
        ),
        migrations.RemoveField(
            model_name='cashflow',
            name='month',
        ),
        migrations.RemoveField(
            model_name='cashflow',
            name='year',
        ),
        migrations.AddField(
            model_name='cashflow',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
