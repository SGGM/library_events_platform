from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "date")
    search_fields = ("title", "date")
    list_filter = (("date", DateRangeFilterBuilder()),)
