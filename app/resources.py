from import_export import resources, fields
from .models import IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition

# Resources of model


class BaseMailResource(resources.ModelResource):
    class Meta:
        exclude = ('id', 'file')
        fields = ('mail_number', 'origin', 'date',
                  'agenda__year', 'user__username')


class IncomingMailResource(BaseMailResource):
    class Meta:
        model = IncomingMail


class OutgoingMailResource(BaseMailResource):
    class Meta:
        model = OutgoingMail


class BaseDispositionResource(resources.ModelResource):
    information = fields.Field(
        attribute='get_information_display'
    )
    
    class Meta:
        exclude = ('id',)
        fields = ('information', 'note', 'mail__mail_number', 'user__username')


class IncomingDispositionResource(BaseDispositionResource):
    class Meta:
        model = IncomingDisposition


class OutgoingDispositionResource(BaseDispositionResource):
    class Meta:
        model = OutgoingDisposition
