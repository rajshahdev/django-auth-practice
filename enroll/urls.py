from django.urls import path
from .views import sign_up, user_login, profile, user_logout,password_with_old, password_with_reset
urlpatterns = [
    path('signup/', sign_up,name='signup'),
    path('login/',user_login,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/',user_logout, name='logout'),
    path('password/',password_with_old, name='password'),
    path('passwordreset/',password_with_reset, name='passwordreset')
]
