from django.urls import path
from.views import index, reserva

from .views import index, reserva

urlpatterns = [
    path('', index),
    path('reserva', reserva),
]