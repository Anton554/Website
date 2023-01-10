from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save_request/', views.save_request)
]