from django.urls import path
from loginlogout import views

urlpatterns = [
    #path('reg/', views.reg, name='reg'),
    path('store_reg/', views.store_reg, name = 'store_reg'),
    #path('home/', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    #path('logout/', views.logout, name = 'logout'),
    path('exit/', views.exit, name='exit'),
    #path('regis/', views.regis, name = 'regis'),
    ]
