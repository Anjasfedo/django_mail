from django.urls import path, reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('reset-password/', views.PasswordResetView.as_view(
        template_name='reset_password.html'), name='reset_password'),
    path('reset-password-done/', views.PasswordResetDoneView.as_view(
        template_name='reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(
        template_name='reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', views.PasswordResetCompleteView.as_view(
        template_name='reset_password_complete.html'), name='password_reset_complete'),
    
    path('password-change/', views.PasswordChangeView.as_view(
        template_name='password_change.html', success_url=reverse_lazy('login')), name='password_change'),
]