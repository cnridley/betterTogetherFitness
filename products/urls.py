from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('guides/', views.guides, name="guides"),
    path('merchandise/', views.merch, name="merch"),
]