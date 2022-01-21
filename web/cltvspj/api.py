from rest_framework import viewsets

from .models import Calculator, ContactEmail
from .serializers import CalculatorSerializer, ContactEmailSerializer


class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer


class ContactEmailViewSet(viewsets.ModelViewSet):
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer
