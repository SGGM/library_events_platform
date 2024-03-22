from django.db import transaction

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.parsers import FormParser, MultiPartParser

import jwt

from .models import Event
from .pagination import SmallPagesPagination
from .tasks import task_execute
from .serializers import (
    CreateEventSerializer,
    EventFullSerializer,
    AllEventsSerializer
)


class EventCreateAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CreateEventSerializer

    def post(self, request, *args, **kwargs):

        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        serializer = CreateEventSerializer(data=request.data)
        if serializer.is_valid():

            instance = serializer.save()
            instance_id = instance.id

            job_params = {"db_id": instance_id}

            transaction.on_commit(lambda: task_execute.delay(job_params))

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EventAPIView(APIView):

    def get(self, request, event_title):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        event = Event.objects.filter(title=event_title).first()
        serializer = EventFullSerializer(event)

        return Response(serializer.data)


class AllEventsAPIView(generics.ListAPIView):
    pagination_class = SmallPagesPagination
    queryset = Event.objects.all()
    serializer_class = AllEventsSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fileds = ["title"]
    filterset_fields = ["date", "title"]
    ordering_fields = ["date"]

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        return self.list(request, *args, **kwargs)
