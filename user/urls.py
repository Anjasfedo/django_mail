from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='reset_password.html'), name='reset_password'),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_password_complete.html'), name='password_reset_complete'),
    
    path('user-profile-update', views.user_profile_update, name='user_profile_update'),
    
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html', success_url=reverse_lazy('login')), name='password_change'),
]