# Generated by Django 3.1.6 on 2021-03-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_auto_20210310_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='recurring',
            field=models.BooleanField(null=True),
        ),
    ]
