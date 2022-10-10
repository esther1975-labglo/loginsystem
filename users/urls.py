from django.urls import path, include
from users.views import dashboard, register, login, login_page, logout_view, user_login, welcome#, my_view, login_page, loginpage, login, Login, login_user
import authentication.views
from django.contrib.auth import views as auth_views
from users import views as user_view

urlpatterns = [
    path("dashboard/", dashboard, name = "dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name = "register"),
    #path("my_view/", my_view, name = "myview"),
    path("login_page/", login_page, name = "login_page"),
    path("logout_view/", logout_view, name = "logout_view"),
    path("login/", login, name = "login"),
    #path("Login/", Login, name = "Login"),
    path("user_login/", user_login, name = "user_login"),
    path("welcome/", welcome, name = "welcome"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   
]
