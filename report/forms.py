from django import forms 
from .models import Report , ReportStatus

class ReportForm(forms.ModelForm):
  class Meta:
    model = Report
    fields = ["location", "Accident_Address", "status", "reporter"]
    

class ReportstatusForm(forms.ModelForm):
  class Meta:
    model = ReportStatus
    fields = "__all__"