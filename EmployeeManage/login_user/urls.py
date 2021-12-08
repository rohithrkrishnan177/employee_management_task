from knox import views as knox_views
from .views import LoginAPI, RegisterAPI
from django.urls import path
from .views import ChangePasswordView
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name='home'),
    path("test",views.test,name='test'),
    path("register_request", views.register_request, name="register_request"),
    path("login_request", views.login_request, name="login_request"),
    path("logout", views.logout_request, name= "logout"),
    path('users/register/', RegisterAPI.as_view(), name='register'),
    path('users/login/', LoginAPI.as_view(), name='login'),
    path('users/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('users/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),

]