from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import os

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
    ('', 'Select Information'),
    (0, 'Processing'),
    (1, 'Accepted'),
    (2, 'Rejected'),
)

# Create your models here.


class Agenda(models.Model):
    '''Model definition for Agenda.'''

    year = models.IntegerField(
        validators=[MinValueValidator(2000), max_value_current_year], unique=True)

    class Meta:
        '''Meta definition for Agenda.'''

        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return str(self.year)


class BaseMail(models.Model):
    '''Model definition for Mail.'''

    mail_number = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)
    file = models.FileField(null=True, blank=True, upload_to="documents/%Y/%m/%d",
                            validators=[validate_file_extension])
    agenda = models.ForeignKey(Agenda, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def file_name(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.mail_number


class IncomingMail(BaseMail):
    class Meta:
        '''Meta definition for IncomingMail.'''

        verbose_name = 'Incoming Mail'
        verbose_name_plural = 'Incoming Mails'


class OutgoingMail(BaseMail):
    class Meta:
        '''Meta definition for OutgoingMail.'''

        verbose_name = 'Outgoing Mail'
        verbose_name_plural = 'Outgoing Mails'


class BaseDisposition(models.Model):
    '''Model definition for Disposition.'''

    information = models.PositiveSmallIntegerField(choices=INFORMATIONS)
    note = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.get_information_display()


class IncomingDisposition(BaseDisposition):
    '''Model definition for IncomingDisposition.'''

    mail = models.OneToOneField(
        IncomingMail, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for IncomingDisposition.'''

        verbose_name = 'Incoming Disposition'
        verbose_name_plural = 'Incoming Dispositions'


class OutgoingDisposition(BaseDisposition):
    '''Model definition for OutgoingDisposition.'''

    mail = models.OneToOneField(
        OutgoingMail, null=True, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for OutgoingDisposition.'''

        verbose_name = 'Outgoing Disposition'
        verbose_name_plural = 'Outgoing Dispositions'
