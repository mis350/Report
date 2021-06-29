from django.db import models

# Create your models here.
class Reporter(models.Model):
  civilid = models.CharField(max_length=50,primary_key=True)
  name = models.CharField(max_length=50)
  address = models.TextField(null=True, blank=True)
  email = models.EmailField()

  def __str__(self):
    return self.name



class Receiver(models.Model):
  ResCivilId = models.CharField(max_length=50)
  ResName = models.CharField(max_length=50)
  email = models.EmailField(blank=True, null=True)

  def __str__(self):
    return self.ResName
  





class Report(models.Model):

    STATUS = (
        (0,"Two car crash"),
        (1,"Multi car crash"),
        (2,"Car crash with Injury"),
        (3,"Car crash with Death"),
        (4,"Car crash with Fire"),
    )

    LOCATION = (
        (0,"Kuwait City"),
        (1,"Al Jahra"),
        (2,"Hawalli"),
        (3,"Farwaniyah"),
        (4,"Mubarak Al-Kabeer"),
        (5, "Al Ahmadi"),
    )

    RSTATUS = (
        (0,"No Traffic Delays"),
        (1," Medium Amount of Traffic"),
        (2, " Traffic Delays"),
    )


    location = models.IntegerField(choices=LOCATION)
    Accident_Address = models.TextField(null=True, blank=True)
    Accident_Describtion = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS)
    created_on = models.DateTimeField(auto_now_add=True)
    RoadStatus = models.IntegerField(choices=RSTATUS, default=0)

    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    receivers = models.ManyToManyField(Receiver, through='ReportStatus')

    def __str__(self):
      return self.Accident_Address





class ReportStatus(models.Model):

    TYPE = (
        (0,"New Report"),
        (1,"In Progress"),
        (2, "Done"),
    )

    Accident_type = models.IntegerField(choices=TYPE, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    Report = models.ForeignKey(Report, on_delete=models.CASCADE)
    def __str__(self):
      return self.Report.Accident_Address