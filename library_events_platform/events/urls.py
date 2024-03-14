from django.urls import path

from .views import EventCreateAPIView, EventAPIView, AllEventsAPIView


urlpatterns = [
    path("event/create/", EventCreateAPIView.as_view()),
    path("event/<str:event_title>/", EventAPIView.as_view()),
    path("all_events/", AllEventsAPIView.as_view()),
]
