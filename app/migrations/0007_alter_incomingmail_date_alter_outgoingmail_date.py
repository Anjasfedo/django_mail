# Generated by Django 5.0.4 on 2024-04-14 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_incomingmail_file_alter_outgoingmail_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingmail',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='outgoingmail',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
