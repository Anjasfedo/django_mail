# Generated by Django 5.0.4 on 2024-04-14 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_incomingmail_date_alter_outgoingmail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingmail',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='outgoingmail',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
