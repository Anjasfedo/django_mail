from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('incoming-mail/', views.incoming_mail, name='incoming_mail'),
    path('incoming-mail-update/<int:pk>/',
         views.incoming_mail_update, name='incoming_mail_update'),
    path('incoming-mail-delete/<int:pk>/',
         views.incoming_mail_delete, name='incoming_mail_delete'),
    path('incoming-mail-export', views.incoming_mail_export,
         name='incoming_mail_export'),

    path('outgoing-mail/', views.outgoing_mail, name='outgoing_mail'),
    path('outgoing-mail-update/<int:pk>/',
         views.outgoing_mail_update, name='outgoing_mail_update'),
    path('outgoing-mail-delete/<int:pk>/',
         views.outgoing_mail_delete, name='outgoing_mail_delete'),
    path('outgoing-mail-export', views.outgoing_mail_export,
         name='outgoing_mail_export'),

    path('incoming-disposition/', views.incoming_disposition,
         name='incoming_disposition'),
    path('incoming-disposition-update/<int:pk>/', views.incoming_disposition_update,
         name='incoming_disposition_update'),
    path('incoming-disposition-delete/<int:pk>/', views.incoming_disposition_delete,
         name='incoming_disposition_delete'),
    path('incoming-disposition-export', views.incoming_disposition_export,
         name='incoming_disposition_export'),

    path('outgoing-disposition/', views.outgoing_disposition,
         name='outgoing_disposition'),
    path('outgoing-disposition-update//<int:pk>/', views.outgoing_disposition_update,
         name='outgoing_disposition_update'),
    path('outgoing-disposition-delete//<int:pk>/', views.outgoing_disposition_delete,
         name='outgoing_disposition_delete'),
    path('outgoing-disposition-export', views.outgoing_disposition_export,
         name='outgoing_disposition_export'),

    path('agenda/', views.agenda, name='agenda'),
    path('agenda-detail/<int:pk>/', views.agenda_detail, name='agenda_detail'),
    path('agenda-detail-incoming-export/<int:pk>/',
         views.agenda_detail_incoming_export, name='agenda_detail_incoming_export'),
    path('agenda-detail-outgoing-export/<int:pk>/',
         views.agenda_detail_outgoing_export, name='agenda_detail_outgoing_export'),
    path('agenda-delete/<int:pk>/', views.agenda_delete, name='agenda_delete'),

     path('user-profile-update', views.user_profile_update, name='user_profile_update'),
]
