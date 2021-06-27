from django.urls import path
from . import views

urlpatterns = [
    path('all/reports', views.all_reports),
    path('all/receiver', views.all_receiver),
    path('all/roads', views.all_roads)

]