
from django.shortcuts import render,redirect
from .models import Profile,Project
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import UserProfile
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView 
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



class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'description','img']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False