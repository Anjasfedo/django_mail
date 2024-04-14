from django.contrib import admin
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition

# Register your models here.

admin.site.register([Agenda, IncomingMail, OutgoingMail,
                    IncomingDisposition, OutgoingDisposition])
