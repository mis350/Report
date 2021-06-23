from django.contrib import admin

# Register your models here.
from .models import Reporter, Report, Receiver, Roads, ReportStatus

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
  list_display = ('name', 'civilid',)



@admin.register(Report)
class RportAdmin(admin.ModelAdmin):
  list_display = ('location', 'reporter', 'status',)
  list_filter = ('status',)
  search_fields = ('location',)


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
  list_display = ('ResName', 'ResCivilId',)

@admin.register(Roads)
class RoadsAdmin(admin.ModelAdmin):
  pass

@admin.register(ReportStatus)
class ReportStatusAdmin(admin.ModelAdmin):
  pass
