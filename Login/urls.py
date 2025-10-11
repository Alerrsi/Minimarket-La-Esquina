from django.urls import path
from Login.views import SpecificUserLoginView,logoutView  

urlpatterns = [
    path("accounts/login", SpecificUserLoginView.as_view(), name = "login"),
    path("accounts/logout",logoutView, name = "logout"),
]