from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.all_reports, name = "all-reports" ),
    path('type/<int:type_id>/', views.accident_type),

    path('show/report/<int:report_id>/', views.report_details),
    path('reporters/', views.reporters, name = "all-reporters"),
    path('show/reporter/<int:reporter_civilid>/', views.reporter_details),
    path('receivers/', views.receivers),
    #path('roads/<int:road_id>/', views.roads_status),
    path('locations/<int:location_id>/', views.location_status),

    path('roads/', views.roads),

    path('add/report/', views.add_report, name = "add-report"),
    path('update/status/', views.update_status),
    path('add/reporter/', views.add_reporter),
    path('show/receiver/<int:receiver_ResCivilId>/', views.receiver_details),

]