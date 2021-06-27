from django.urls import path
from . import views

urlpatterns = [
    path('all/reports', views.all_reports, name = "all-reports" ),
    #path('all/reports2', views.all_reports2),
    #path('new/reports', views.new_reports),
    path('type/<int:type_id>/', views.accident_type),
    path('show/report/<int:report_id>/', views.report_details),
    path('show/reporters/', views.reporters),
    path('show/reporter/<int:reporter_civilid>/', views.reporter_details),
    path('show/receiver/', views.receivers),
    path('all/receiver', views.all_receiver),
    path('all/roads', views.all_roads),
    path('add/report', views.add_report, name = "add-report"),
    path('update/status', views.update_status),

]