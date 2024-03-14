from rest_framework import serializers

from .models import Event
from organizations.serializers import OrganizationSerializer


class CreateEventSerializer(serializers.ModelSerializer):

    image = serializers.FileField(required=False)

    class Meta:
        model = Event
        fields = ("title", "description", "organizations", "image", "date")

class EventFullSerializer(serializers.ModelSerializer):

    image = serializers.FileField(required=False)
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "title", "description", "date", "image", "organizations")

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"

class AllEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("title", "date")