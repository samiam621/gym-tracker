from django.contrib import admin
from .models import GymVisit


@admin.register(GymVisit)
class GymVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('user__username',)
