from django.urls import path
from . import  views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('mini_projects', views.miniProjects, name='miniProjects'),
    path('final_projects', views.finalProjects, name='finalProjects'),
    path('hackathon', views.hackathon, name='hackathon'),
    path('internship', views.internship, name='internship'),
]
