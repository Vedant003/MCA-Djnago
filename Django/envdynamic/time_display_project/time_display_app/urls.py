from django.urls import path
from .views import time_after_10_hours

urlpatterns = [
    path('time_after_10_hours/<int:hours>/', time_after_10_hours, name='time_after_10_hours'),
]
