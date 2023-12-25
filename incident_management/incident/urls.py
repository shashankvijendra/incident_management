from .views import *
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
   path('incidents/<str:pk>',IncidentAPIView.as_view()),
]

