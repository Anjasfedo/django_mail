from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Utils Function


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


INFORMATIONS = (
    (0, 'Processing'),
    (1, 'Accepted'),
    (2, 'Rejected'),
)

# Create your models here.


class Agenda(models.Model):
    '''Model definition for Agenda.'''

    year = models.IntegerField(
        validators=[MinValueValidator(2000), max_value_current_year])

    class Meta:
        '''Meta definition for Agenda.'''

        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return str(self.year)


class IncomingMail(models.Model):
    '''Model definition for IncomingMail.'''

    mail_number = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)
    file = models.FileField(null=True, upload_to="documents/%Y/%m/%d",
                            validators=[validate_file_extension])
    agenda = models.ForeignKey(Agenda, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for IncomingMail.'''

        verbose_name = 'IncomingMail'
        verbose_name_plural = 'IncomingMails'

    def __str__(self):
        return self.mail_number


class OutgoingMail(models.Model):
    '''Model definition for OutgoingMail.'''

    mail_number = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)
    file = models.FileField(null=True, upload_to="documents/%Y/%m/%d",
                            validators=[validate_file_extension])
    agenda = models.ForeignKey(Agenda, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for OutgoingMail.'''

        verbose_name = 'OutgoingMail'
        verbose_name_plural = 'OutgoingMails'

    def __str__(self):
        return self.mail_number


class IncomingDisposition(models.Model):
    '''Model definition for IncomingDisposition.'''

    information = models.PositiveSmallIntegerField(choices=INFORMATIONS)
    note = models.CharField(max_length=200)
    mail = models.OneToOneField(
        IncomingMail, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for IncomingDisposition.'''

        verbose_name = 'IncomingDisposition'
        verbose_name_plural = 'IncomingDispositions'

    def __str__(self):
        return self.get_information_display()


class OutgoingDisposition(models.Model):
    '''Model definition for OutgoingDisposition.'''

    information = models.PositiveSmallIntegerField(choices=INFORMATIONS)
    note = models.CharField(max_length=200)
    mail = models.OneToOneField(
        OutgoingMail, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for OutgoingDisposition.'''

        verbose_name = 'OutgoingDisposition'
        verbose_name_plural = 'OutgoingDispositions'

    def __str__(self):
        return self.get_information_display()
