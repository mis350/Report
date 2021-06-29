from django.contrib import admin

# Register your models here.
from .models import Reporter, Report, Receiver, ReportStatus

class ReportInLine(admin.TabularInline):
  model = Report

class ReportStatusInLine(admin.TabularInline):
  model = ReportStatus

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
  list_display = ('name', 'civilid',)
  inlines = (ReportInLine,)



@admin.register(Report)
class RportAdmin(admin.ModelAdmin):
  list_display = ('id','location','Accident_Address', 'reporter', 'status', 'created_on', 'RoadStatus')
  list_filter = ('status','location','RoadStatus')
  search_fields = ('location',)
  inlines = (ReportStatusInLine,)






@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
  list_display = ('ResName', 'ResCivilId',)
  inlines = (ReportStatusInLine,)




@admin.register(ReportStatus)
class ReportStatusAdmin(admin.ModelAdmin):
  list_display = ('Report','receiver','Accident_type')
  list_filter = ('Accident_type',)