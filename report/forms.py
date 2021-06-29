from django import forms 
from .models import Report , ReportStatus, Reporter

class ReportForm(forms.ModelForm):
  class Meta:
    model = Report
    fields = ['location', 'Accident_Address', 'Accident_Describtion', 'status', 'RoadStatus', 'reporter']
    

class ReportstatusForm(forms.ModelForm):
  class Meta:
    model = ReportStatus
    fields = "__all__"

class ReporterForm(forms.ModelForm):
  class Meta:
    model = Reporter
    fields = "__all__"