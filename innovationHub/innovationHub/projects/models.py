from asyncio import streams
from operator import mod
from pyexpat import model
from sre_constants import BRANCH, CATEGORY
from statistics import mode
from django.db import models

import projects

# Create your models here.
BRANCHES = (
    ('Civil', 'Civil'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('Mech', 'Mech'),
)

CATEGORY = (
    ('MINI_PROJECT', 'MINI_PROJECT'),
    ('FINAL_PROJECT', 'FINAL_PROJECT'),
)


class Project(models.Model):
    
    roll_no = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    branch = models.CharField(choices=BRANCHES, max_length=20)
    category = models.CharField(choices=CATEGORY, max_length=20)
    year = models.CharField(max_length=10)
    project_title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    document = models.CharField(max_length=100)
    video = models.CharField(max_length=100, null=True, blank=True)


    date_created = models.DateField(auto_now_add=True, null=True)