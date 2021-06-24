from django.urls import path
from . import views

urlpatterns = [
    path('all/reports', views.all_reports),
    path('new/reports', views.new_reports),
    path('type/<int:type_id>/', views.accident_type),
    path('show/report/<int:report_id>/', views.report_details),
]