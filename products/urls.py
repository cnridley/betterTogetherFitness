from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.guides, name="guides"),
    path('', views.merch, name="merch"),
]