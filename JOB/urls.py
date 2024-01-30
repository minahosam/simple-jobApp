from django.urls import path
from .views import *

app_name = 'job'

urlpatterns = [
    path('all-jobs',all_jobs,name='jobs'),
    path('job/<slug>/',get_job,name='job'),
]