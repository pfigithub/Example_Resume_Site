from . import views
from django.urls import path
from allauth.account.views import LogoutView, LoginView, SignupView

app_name = 'accounts'

urlpatterns = [

    path('/accounts/login/', LoginView, name='account_login'),
    path('/accounts/logout/', LogoutView, name='account_logout'),
    path('/accounts/signup/', SignupView, name='account_signup')
   
]