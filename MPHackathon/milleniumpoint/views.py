from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    sampleString = "We rock!"
    return render(request, 'base.html', {'headline':sampleString})