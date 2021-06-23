from django.contrib import admin

# Register your models here.
from .models import Reporter, Report, Receiver, Roads

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
  pass

@admin.register(Report)
class RportAdmin(admin.ModelAdmin):
  pass

@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
  pass

@admin.register(Roads)
class RoadsAdmin(admin.ModelAdmin):
  pass