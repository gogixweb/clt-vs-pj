from rest_framework import serializers

from .models import Calculator, ContactEmail


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = [
            "clt",
            "pj",
        ]


class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = [
            "email",
            "subject",
        ]
