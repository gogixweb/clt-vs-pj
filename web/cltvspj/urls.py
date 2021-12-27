from django.urls import path, include
from . import views

from rest_framework import routers
from .api import CalculatorViewSet

api_router = routers.DefaultRouter()
api_router.register("calculator", CalculatorViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("api/v1/", include(api_router.urls)),
]
