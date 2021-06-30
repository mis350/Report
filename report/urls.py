from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.all_reports, name = "all-reports" ),
    path('type/<int:type_id>/', views.accident_type),


    path('show/report/<int:report_id>/', views.report_details, name = 'show-report'),
    path('reporters/', views.reporters, name = "all-reporters"),
    path('receivers/', views.receivers, name = "all-receivers"),


    path('show/report/<int:report_id>/', views.report_details, name = 'show-report'),    
    path('show/reporter/<int:reporter_civilid>/', views.reporter_details, name = 'show-reporter'),
    path('show/receiver/<int:receiver_ResCivilId>/', views.receiver_details, name = 'show-receiver'),


    path('roads/', views.roads, name = "roads"),
    path('locations/<int:location_id>/', views.location_status),


    path('add/report/', views.add_report, name = "add-report"), 
    path('add/reporter/', views.add_reporter),
    path('add/receiver/', views.add_receiver),
    
    path('delete/report/<int:report_id>/',views.delete_report, name="delete-report"),
    path('delete/reporter/<int:reporter_civilid>/',views.delete_reporter, name="delete-reporter"),
    path('delete/receiver/<int:receiver_ResCivilId>/',views.delete_receiver, name="delete-receiver"),

    path('edit/report/<int:report_id>/', views.edit_report, name = 'edit-report'),
    path('edit/reporter/<int:reporter_civilid>/', views.edit_reporter, name = 'edit-report'),
    path('edit/receiver/<int:receiver_ResCivilId>/', views.edit_receiver, name = 'edit-receiver'),
]