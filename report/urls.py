from django.urls import path
from . import views

urlpatterns = [
    path('all/reports', views.all_reports),



    #path('all/reports2', views.all_reports2),
    #path('new/reports', views.new_reports),
    path('type/<int:type_id>/', views.accident_type),
    path('show/report/<int:report_id>/', views.report_details),
    path('show/reporter/<int:reporter_civilid>/', views.reporter_details),
    path('show/receiver/<int:receiver_id>/', views.receiver_details),
    path('all/receiver', views.all_receiver),
    path('all/roads', views.all_roads),

]