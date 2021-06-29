from django.shortcuts import render, redirect, get_object_or_404

from .models import Report, ReportStatus , Reporter , Receiver
from .forms import ReportForm, ReporterForm, ReceiverForm

# Create your views here.




#perfect.
def all_reports(request):
  data={}
  reports = Report.objects.all()
  data['reports'] = reports
  return render(request, "all_reports.html", context=data)




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
  data["receviers"] = receiver
  return render(request, "receivers.html", context = data)


#perfect.
def reporter_details(request, reporter_civilid):
  data={}
  reporters = Reporter.objects.get(civilid = reporter_civilid)
  report_list = reporters.report_set.all()
  data["reporter"] = reporters
  data["report"] = report_list
  return render(request, "reporter_details.html", context = data)


#perfect.
def receiver_details(request, receiver_ResCivilId):
  data={}
  receiver = Receiver.objects.get(ResCivilId = receiver_ResCivilId)
  reports = receiver.report_set.all()
  data['report'] = reports
  data['receiver'] = receiver
  return render(request, "receiver_details.html", context=data)




 
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



def add_reporter(request):
  data={}
  f = ReporterForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("all-reporters")
  return render(request, "add_reporter.html", context = data)



def add_receiver(request):
  data={}
  f = ReceiverForm(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("all-receivers")
  return render(request, "add_receiver.html", context = data)


# Edit 

def edit_report(request, report_id):
  r = get_object_or_404(Report, id=report_id)
  f = ReportForm(request.POST or None, instance=r)

  data = {
    "form": f,
    "report": r,
  }

  if f.is_valid():
    report = f.save(commit=False)
    report.save()
    return redirect("show-report", report_id = report.id)
  return render(request, "edit_report.html", context=data)


def edit_reporter(request, reporter_civilid):
  r = get_object_or_404(Reporter, civilid=reporter_civilid)
  f = ReporterForm(request.POST or None, instance=r)

  data = {
    "form": f,
    "reporter": r,
  }

  if f.is_valid():
    reporter = f.save(commit=False)
    reporter.save()
    return redirect("show-reporter", reporter_civilid = reporter.civilid)
  return render(request, "edit_reporter.html", context=data)

def edit_receiver(request, receiver_ResCivilId):
  r = get_object_or_404(Receiver, ResCivilId=receiver_ResCivilId)
  f = ReceiverForm(request.POST or None, instance=r)

  data = {
    "form": f,
    "receiver": r,
  }

  if f.is_valid():
    receiver = f.save(commit=False)
    receiver.save()
    return redirect("show-receiver", receiver_ResCivilId = receiver.ResCivilId)
  return render(request, "edit_receiver.html", context=data)

# Delete


def delete_report(request, report_id):
  r = get_object_or_404(Report, id=report_id)
  m = f"Do you really want to delete {r.Accident_Address} report?"
  data = {
    "message": m,
  }
  if "confirm" in request.GET:
    r.delete()
    return redirect("all-reports")
  elif "cancel" in request.GET:
    return redirect("all-reports")
  else:
    return render(request, "confirm.html", context=data)


def delete_reporter(request, reporter_civilid):
  r = get_object_or_404(Reporter, civilid=reporter_civilid)
  m = f"Do you really want to delete {r.name} from the Reperters list?"
  data = {
    "message": m,
  }
  if "confirm" in request.GET:
    r.delete()
    return redirect("all-reporters")
  elif "cancel" in request.GET:
    return redirect("all-reporters")
  else:
    return render(request, "confirm.html", context=data)


def delete_receiver(request, receiver_ResCivilId):
  r = get_object_or_404(Receiver, ResCivilId=receiver_ResCivilId)
  m = f"Do you really want to delete {r.ResName} from the Receiver list?"
  data = {
    "message": m,
  }
  if "confirm" in request.GET:
    r.delete()
    return redirect("all-receivers")
  elif "cancel" in request.GET:
    return redirect("all-receivers")
  else:
    return render(request, "confirm.html", context=data)