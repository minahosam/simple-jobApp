from django.db import models

# Create your models here.

Job_Type = (('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Intetship', 'Intetship'))

class job(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,null=True)
    salary = models.IntegerField(default=1)
    location = models.CharField(max_length=10000,null=True)
    type = models.CharField(choices = Job_Type, max_length=20,default='Full Time')
    slug = models.SlugField()
    