from django.db import models

# Create your models here.
class Hospital(models.Model):
    Hospital = models.CharField(max_length=255 ,default=" ")
    County   = models.CharField(max_length=255 ,default=" ")
    City     = models.CharField(max_length=255 ,default=" ")
    csv_file = models.FileField(upload_to='documents', default=" ")
    def __str__(self):
        return self.Hospital