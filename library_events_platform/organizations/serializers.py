from rest_framework import serializers

from .models import Organization
from users.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):

    employees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ("title", "description", "address", "postcode", "employees")
