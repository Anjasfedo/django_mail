from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('incoming-mail/', views.incoming_mail, name='incoming_mail'),
    path('incoming-mail-update/<int:pk>/',
         views.incoming_mail_update, name='incoming_mail_update'),
    path('incoming-mail-delete/<int:pk>/',
         views.incoming_mail_delete, name='incoming_mail_delete'),

    path('outgoing-mail/', views.outgoing_mail, name='outgoing_mail'),
    path('outgoing-mail-update/<int:pk>/',
         views.outgoing_mail_update, name='outgoing_mail_update'),
    path('outgoing-mail-delete/<int:pk>/',
         views.outgoing_mail_delete, name='outgoing_mail_delete'),

    path('incoming-disposition/', views.incoming_disposition,
         name='incoming_disposition'),
    path('incoming-disposition-update/<int:pk>/', views.incoming_disposition_update,
         name='incoming_disposition_update'),
    path('incoming-disposition-delete/<int:pk>/', views.incoming_disposition_delete,
         name='incoming_disposition_delete'),

    path('outgoing-disposition/', views.outgoing_disposition,
         name='outgoing_disposition'),
    path('outgoing-disposition-update//<int:pk>/', views.outgoing_disposition_update,
         name='outgoing_disposition_update'),
    path('outgoing-disposition-delete//<int:pk>/', views.outgoing_disposition_delete,
         name='outgoing_disposition_delete'),

    path('agenda/', views.agenda, name='agenda'),
    path('agenda-update/<int:pk>/', views.agenda_update, name='agenda_update'),
    path('agenda-delete/<int:pk>/', views.agenda_delete, name='agenda_delete'),

]
