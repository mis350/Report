from django.shortcuts import render
from .models import Report

# Create your views here.


def all_reports(request):
  data={}
  reports = Report.objects.all
  data['reports'] = reports
  #data['location'] = reports.objects.get_location_display()
  #data['location'] = reports.objects.get_location_display()
  return render(request, "all_reports.html", context=data)