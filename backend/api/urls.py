from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('toggle/', views.toggle_visit, name='toggle_visit'),
]
