from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def index(request):
    date = []
    other = []
    other1 = []
    other2 = []
    other3 = []
    other4 = []

    sampleString = "We rock the world!"
    with open("MPDD.csv") as csvfile:
        for row in csvfile:
            a = row.split(",")
            if len(a) == 1:
                continue
            date.append(a[0])
            other.append((a[2]))
            other1.append((a[3]))
            other2.append((a[4]))
            other3.append((a[5]))
            other4.append((a[6]))
    return render(request, 'base.html', {'dates':date, 'other':other, 'other1':other1,'other2':other2,'other3':other3, 'other4':other4})