from django.shortcuts import render
import csv
from .models import Csv_date
# Create your views here.

# r=csv.reader((csvf)) #returns csv reader object
# data=list(r)

def format_date(date):
    #print(date.split('/'))
    year  = date.split('-')[0]
    month = date.split('-')[1]
    dt  = date.split('-')[2]
    return '%s-%s-%s' %(year, month, dt) # eg: '2017-05-01'


csvf=open("csv_to_database/out.csv",'r')
reader = csv.DictReader(csvf)

for row in reader:
    #print(row['date'].split('-'))
    date = format_date(row['date'])
    Csv_date.objects.create(date=date)

def csv_to_date(request):
    dates=Csv_date.objects.all()
    return render(request,'csv_to_database/home.html',{'dates':dates})

