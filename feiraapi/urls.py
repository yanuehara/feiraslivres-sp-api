from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('feiras/', views.FeirasList.as_view(), name='feira-list'),
    path('feira/<int:pk>/', views.FeiraDetails.as_view(), name='feira-details'),
]

