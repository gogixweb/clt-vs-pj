from django.urls import path, include
from . import views

from rest_framework import routers
from .api import CalculatorViewSet, ContactEmailViewSet

calculator = routers.DefaultRouter()
calculator.register("calculator", CalculatorViewSet)
contact_email = routers.DefaultRouter()
contact_email.register("contact", ContactEmailViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("contact_email", views.contact_email, name='contact_email'),
    path("api/v1/", include(calculator.urls)),
    path("api/v1/", include(contact_email.urls)),
]
