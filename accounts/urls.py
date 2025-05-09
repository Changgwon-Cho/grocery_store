from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/accounts/password_change_done/'
    ), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
]