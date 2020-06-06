
from django.shortcuts import render,redirect
from .models import Profile,Project
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import UserProfile
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def welcome(request):

        context ={
             'projects':Project.objects.all()
    }
    
        return render(request,'fold/welcome.html',context)
class ProjectListView(ListView):
    model = Project
    template_name = 'fold/welcome.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project