from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('incoming-mail', views.incoming_mail, name='incoming_mail')
]
