# Generated by Django 3.1.6 on 2021-03-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0044_merge_20210316_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow',
            name='recurring',
        ),
        migrations.AddField(
            model_name='cashflow',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Transportation', 'Transportation'), ('Groceries', 'Groceries'), ('Health', 'Health'), ('Shopping & Entertainment', 'Shopping & Entertainemnt'), ('Other', 'Other')], default='Food', max_length=26, null=True),
        ),
    ]
