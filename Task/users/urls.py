from django.urls import path
from .views import EventView

urlpatterns = [
    path('test/', EventView.as_view())
]