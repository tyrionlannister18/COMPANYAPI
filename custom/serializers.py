from rest_framework import serializers
from .models import Company

class CompanySer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
