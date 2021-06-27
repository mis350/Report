from django.contrib import admin

# Register your models here.
from .models import Reporter, Report, Receiver, Roads, ReportStatus

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
  list_display = ('location', 'reporter', 'status',)
  list_filter = ('status','location',)
  search_fields = ('location',)
  inlines = (ReportStatusInLine,)






@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
  list_display = ('ResName', 'ResCivilId',)
  inlines = (ReportStatusInLine,)


@admin.register(Roads)
class RoadsAdmin(admin.ModelAdmin):
  pass

@admin.register(ReportStatus)
class ReportStatusAdmin(admin.ModelAdmin):
  list_display = ('Report','receiver','Accident_type')
  list_filter = ('Accident_type',)