from django.shortcuts import render
from .models import Report   
from .models import Receiver
from .models import Roads
# Create your views here.


def all_reports(request):
  data={}
  reports = Report.objects.all
  data['reports'] = reports
  #data['location'] = reports.objects.get_location_display()
  #data['location'] = reports.objects.get_location_display()
  return render(request, "all_reports.html", context=data)

def all_receiver(request):
  data={}
  receiver = Receiver.objects.all
  data['receiver'] = receiver
  return render(request, "all_receiver.html", context=data)

def all_roads(request):
  data={}
  roads = Roads.objects.all
  data['roads'] = roads
  return render(request, "all_roads.html", context=data)