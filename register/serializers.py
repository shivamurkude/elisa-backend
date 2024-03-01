from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    session = serializers.ListField(child=serializers.CharField(max_length=20, allow_blank=True, allow_null=True), required=False)

    class Meta:
        model = Registration
        fields = '__all__'
