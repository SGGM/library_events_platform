from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "address", "postcode")
    search_fields = ("title", "description", "address", "postcode")
    list_filter = ("title", "address", "postcode")
