from django.urls import path
from .views import RegisterView,loginView,logoutView

urlpatterns=[
    path('register',RegisterView.as_view(),name="RegisterView"),
    path('login',loginView.as_view(),name="loginView"),
    path('logout',logoutView.as_view(),name="logoutView")
]
