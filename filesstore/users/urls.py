from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Logout, Session
from . import createUser

urlpatterns = [
    path('login/', obtain_auth_token, name='user-login'),
    path('logout/',  Logout.as_view(), name='user-logout'),
    path('session/',  Session.as_view(), name='user-session'),
    path('registration/', createUser.CreateUser.as_view(), name='user-new')
]