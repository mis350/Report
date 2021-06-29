from django.shortcuts import render, redirect

from .models import Report, ReportStatus , Reporter , Receiver
from .forms import ReportForm, ReportstatusForm, ReporterForm

# Create your views here.

#perfect.
def all_reports(request):
  data={}
  reports = Report.objects.all()
  data['reports'] = reports
  return render(request, "all_reports.html", context=data)

#perfect.
def receiver_details(request, receiver_ResCivilId):
  data={}
  receiver = Receiver.objects.get(ResCivilId = receiver_ResCivilId)
  reports = receiver.report_set.all()
  data['report'] = reports
  data['receiver'] = receiver
  return render(request, "receiver_details.html", context=data)



#NOTHING TO SHOW!!!!!!!!!!
def accident_type(request,type_id):
  data = {}
  type_list = ReportStatus.objects.filter(Accident_type = type_id)

  if type_id == 0:
    data["title"] = "New Report"
  elif type_id == 1:
    data["title"] = "In Progress Report"
  else:
    data["title"] = "Done"

  data["accident_type"] = type_list
  return render(request, "accident_type.html", context = data)



# just add link inside to the reporter / receiver
def report_details(request, report_id):
  data={}
  reports = Report.objects.get(id = report_id)
  Acc_type = reports.reportstatus_set.all()
  for a in Acc_type:
    if a.Accident_type == 1:
      data["Typee"] = "In Progress Report"
    if a.Accident_type == 2:
      data["Typee"] = "Done"
    else:
      data["Typee"] = "New Report"
  
  data["reports"] = reports
  data["Type"] = Acc_type 
  return render(request, "report_details.html", context = data)




#perfect.
def reporter_details(request, reporter_civilid):
  data={}
  reporters = Reporter.objects.get(civilid = reporter_civilid)
  report_list = reporters.report_set.all()
  data["reporter"] = reporters
  data["report"] = report_list
  return render(request, "reporter_details.html", context = data)



#perfect.
def reporters(request):
  data={}
  reporters = Reporter.objects.all()
  #report_list = reporters.report_set.all()
  data["reporters"] = reporters
  #data["report"] = report_list
  return render(request, "reporters.html", context = data)




#perfect.
def receivers(request):
  data={}
  receiver = Receiver.objects.all()
  #status = receiver.reportstatus_set.all()
  #reciver = status.receiver_set.all()
  data["receviers"] = receiver
  #data["status"] = status
  #data["reciver"] = reciver
  return render(request, "receivers.html", context = data)




#As a filter
#def roads_status(request,road_id):
  #roadstatus = Report.objects.filter(RoadStatus = road_id)
  #data = {}
  #data["roads"] = roadstatus 
  #return render(request, "roads_status.html", context = data)
 
#Perfect
def location_status(request,location_id):
  locationstatus = Report.objects.filter(location = location_id)
  data = {}
  data["locations"] = locationstatus 
  return render(request, "location_status.html", context = data)

def roads(request):
  data={}
  reports = Report.objects.all()
  data['reports'] = reports
  return render(request, "roads.html", context=data)

def add_report(request):
  data={}
  f = ReportForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("all-reports")
  return render(request, "add_report.html", context = data)




def update_status(request):
  data={}
  f = ReportstatusForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("all-reports")
  return render(request, "update_status.html", context = data)


def add_reporter(request):
  data={}
  f = ReporterForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("all-reporters")
  return render(request, "add_reporter.html", context = data)


