# Generated by Django 3.1.6 on 2021-03-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_payments_paymentorincome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='paymentOrIncome',
            field=models.CharField(choices=[('payment', 'payment'), ('income', 'income')], default='payment', max_length=26, null=True),
        ),
    ]
