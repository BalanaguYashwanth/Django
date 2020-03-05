from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('base',views.base,name='base'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('delete/<list_id>/',views.delete,name="delete"),
];


