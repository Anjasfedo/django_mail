from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('incoming-mail', views.incoming_mail, name='incoming_mail'),
    path('outgoing-mail', views.outgoing_mail, name='outgoing_mail'),
    path('incoming-disposition', views.incoming_disposition,
         name='incoming_disposition'),
    path('incoming-disposition', views.incoming_disposition,
         name='incoming_disposition'),
    path('agenda', views.agenda, name='agenda'),
]
