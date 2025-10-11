from django.urls import path
from .views import index, direct

urlpatterns = [
    path("inicio/", index, name = "index"),
    path("", direct, name="direct")
]