from django.shortcuts import render
from .models import *

# Create your views here.

def all_jobs(request):
    all = job.objects.all()
    context = {'jobs': all}
    return render(request,'jobs/index.html',context)

def get_job(request,slug):
    single_job = job.objects.get(slug=slug)
    context = {'job':single_job}
    return render(request,'jobs/single_job.html',context)