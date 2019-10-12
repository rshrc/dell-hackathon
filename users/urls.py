from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from users.views import UserView, register

app_name = 'users'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='user/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('profile/', login_required(UserView.as_view()), name='profile'),
    path('register/', register, name='register'),
]