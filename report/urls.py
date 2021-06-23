from django.urls import path
from . import views

urlpatterns = [
    path('all/reports', views.all_reports),
]