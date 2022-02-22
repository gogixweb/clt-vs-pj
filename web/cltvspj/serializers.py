from rest_framework import serializers

from .models import Calculator


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = [
            "clt",
            "pj",
        ]
