# Generated by Django 3.1.6 on 2021-03-16 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0040_auto_20210315_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
