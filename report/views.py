from django.shortcuts import render
from .models import Report, ReportStatus # , Reporter
# Create your views here.

#Proplems: location + status + Reporter name
def all_reports(request):
  data={}
  reports = Report.objects.all()
  data['reports'] = reports
  return render(request, "all_reports.html", context=data)



#No need - nothing showing
def new_reports(request):
  data={}
  reports = ReportStatus.objects.filter(Accident_type=0)
  data['new_reports'] = reports
  return render(request, "new_reports.html", context=data)



#works, problems: report + reciever name
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
  #data["report"] = type_list.report_set.all()

  return render(request, "accident_type.html", context = data)



#works, but nothing showen
def report_details(request, report_id):
  data={}
  reports = Report.objects.get(id = report_id)
  data["reports"] = reports
  return render(request, "report_details.html", context = data)


