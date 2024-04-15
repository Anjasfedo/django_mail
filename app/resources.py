from import_export import resources, fields
from .models import IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition, Agenda

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


class BaseAgendaDetailResource(resources.ModelResource):
    class Meta:
        abstract = True

    def get_queryset(self):
        return self._meta.model.objects.none()


class IncomingAgendaDetailResource(BaseAgendaDetailResource):
    class Meta(BaseAgendaDetailResource.Meta):
        model = IncomingMail
        fields = ('incoming_mail_number', 'incoming_information',
                  'incoming_origin', 'incoming_date')
        export_order = fields

    incoming_mail_number = fields.Field(
        attribute='incoming_mail__mail_number', column_name='Incoming Mail Number')
    incoming_information = fields.Field(
        attribute='incoming_disposition__information', column_name='Incoming Information')
    incoming_origin = fields.Field(
        attribute='incoming_mail__origin', column_name='Incoming Origin')
    incoming_date = fields.Field(
        attribute='incoming_mail__date', column_name='Incoming Date')

    def dehydrate_incoming_information(self, incoming_data):
        incoming_mail, incoming_disposition = incoming_data
        return incoming_disposition.get_information_display() if incoming_disposition else ''

    def dehydrate_incoming_mail_number(self, incoming_data):
        incoming_mail, incoming_disposition = incoming_data
        return incoming_mail.mail_number if incoming_mail else ''

    def dehydrate_incoming_origin(self, incoming_data):
        incoming_mail, incoming_disposition = incoming_data
        return incoming_mail.origin if incoming_mail else ''

    def dehydrate_incoming_date(self, incoming_data):
        incoming_mail, incoming_disposition = incoming_data
        return incoming_mail.date.strftime('%Y-%m-%d') if incoming_mail else None


class OutgoingAgendaDetailResource(BaseAgendaDetailResource):
    class Meta(BaseAgendaDetailResource.Meta):
        model = OutgoingMail
        fields = ('outgoing_mail_number', 'outgoing_information',
                  'outgoing_origin', 'outgoing_date')
        export_order = fields

    outgoing_mail_number = fields.Field(
        attribute='outgoing_mail__mail_number', column_name='Outgoing Mail Number')
    outgoing_information = fields.Field(
        attribute='outgoing_disposition__information', column_name='Outgoing Information')
    outgoing_origin = fields.Field(
        attribute='outgoing_mail__origin', column_name='Outgoing Origin')
    outgoing_date = fields.Field(
        attribute='outgoing_mail__date', column_name='Outgoing Date')

    def dehydrate_outgoing_mail_number(self, outgoing_data):
        outgoing_mail, outgoing_disposition = outgoing_data
        return outgoing_mail.mail_number if outgoing_mail else ''

    def dehydrate_outgoing_information(self, outgoing_data):
        outgoing_mail, outgoing_disposition = outgoing_data
        return outgoing_disposition.get_information_display() if outgoing_disposition else ''

    def dehydrate_outgoing_origin(self, outgoing_data):
        outgoing_mail, outgoing_disposition = outgoing_data
        return outgoing_mail.origin if outgoing_mail else ''

    def dehydrate_outgoing_date(self, outgoing_data):
        outgoing_mail, outgoing_disposition = outgoing_data
        return outgoing_mail.date.strftime('%Y-%m-%d') if outgoing_mail else None
