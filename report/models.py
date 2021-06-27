from django.db import models

# Create your models here.
class Reporter(models.Model):
 # civilid = models.IntegerField(primary_key=True)
  civilid = models.CharField(max_length=50,primary_key=True)
  name = models.CharField(max_length=50)
  address = models.TextField(null=True, blank=True)
  email = models.EmailField()

  def __str__(self):
    return self.name



class Receiver(models.Model):
  ResCivilId = models.CharField(max_length=50)
  ResName = models.CharField(max_length=50)

  def __str__(self):
    return self.ResName
  

class Roads(models.Model):
  RoadNo = models.CharField(max_length=50)
  RoadName = models.TextField(null=False, blank=False)



class Report(models.Model):

    #TYPE = (
       # (0,"New Report"),
       # (1,"In Progress"),
       # (2, "Done"),
   # )



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


    #Road_name = models.TextField()
    #Accident_type = models.IntegerField(choices=TYPE, default=0)
  #image = models.
    location = models.IntegerField(choices=LOCATION)
    #location = models.CharField(max_length=50, choices=LOCATION)
    Accident_Address = models.TextField(null=True, blank=True)
    Accident_Describtion = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    #receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    def __str__(self):
      return self.Accident_Address



class ReportStatus(models.Model):

    TYPE = (
        (0,"New Report"),
        (1,"In Progress"),
        (2, "Done"),
    )

    Accident_type = models.IntegerField(choices=TYPE, default=0)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    Report = models.ForeignKey(Report, on_delete=models.CASCADE)
    #Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    #def __str__(self):
      #return self.location
    def __str__(self):
      return self.Report.Accident_Address
    
