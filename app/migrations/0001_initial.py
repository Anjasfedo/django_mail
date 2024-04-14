# Generated by Django 5.0.4 on 2024-04-14 07:36

import app.models
import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), app.models.max_value_current_year])),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
        migrations.CreateModel(
            name='IncomingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_number', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('file', models.FileField(null=True, upload_to='', validators=[app.models.validate_file_extension])),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agenda')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'IncomingMail',
                'verbose_name_plural': 'IncomingMails',
            },
        ),
        migrations.CreateModel(
            name='OutgoingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_number', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('file', models.FileField(null=True, upload_to='documents/%Y/%m/%d', validators=[app.models.validate_file_extension])),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.agenda')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OutgoingMail',
                'verbose_name_plural': 'OutgoingMails',
            },
        ),
    ]
