from rest_framework import viewsets

from .models import Calculator
from .serializers import CalculatorSerializer


class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer
