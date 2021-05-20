from django.db import models

# Create your models here.
class Csv_date(models.Model):
    date=models.DateField(auto_now=False,auto_now_add=False)
    