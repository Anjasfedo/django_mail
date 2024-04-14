from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('incoming-mail/', views.incoming_mail, name='incoming_mail'),
    path('incoming-mail-update/<int:pk>/', views.incoming_mail_update, name='incoming_mail_update'),
    
    path('outgoing-mail/', views.outgoing_mail, name='outgoing_mail'),
    
    path('incoming-disposition/', views.incoming_disposition,
         name='incoming_disposition'),
    
    path('outgoing-disposition/', views.outgoing_disposition,
         name='outgoing_disposition'),
    
    path('agenda/', views.agenda, name='agenda'),
    path('agenda-update/<int:pk>/', views.agenda_update, name='agenda_update'),
    path('agenda-delete/<int:pk>/', views.agenda_delete, name='agenda_delete'),
    
]
