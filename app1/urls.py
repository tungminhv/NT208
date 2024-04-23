from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup_in/',views.signup_in , name='signup_in'),
    path('timgiasu/',views.find , name='find'),
    path('giasu/',views.tutor ,name='tutor'),
    path('signout/', views.signout, name='signout'),
    path('timgiasu/info/', views.info, name='info'),

    #reset password
    path('signup_in/reset_pass/', views.reset_pass, name='reset_pass'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app/reset_password_mail.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/reset_password.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app/reset_password_complete.html"), name="password_reset_complete"),
]