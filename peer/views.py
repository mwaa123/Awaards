
from django.shortcuts import render,redirect
from .models import Profile,Project
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from .forms import VoteForm
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

def search_results(request):
    if 'search_title' in request.GET and request.GET["search_title"]:
        search_term = request.GET.get("search_title")
        searched_titles = User.objects.filter(username__icontains=search_term)
        message=search_term

        return render(request,"peer/search.html", {"images":searched_titles, "message":message}) 


    else:
        message = "Search term not found"  

        return render(request,'peer/search.html',{"message":message})



 
class VoteCreateView(LoginRequiredMixin,CreateView):
    model = Vote
    fields = ['design_votes', 'usability_votes', 'creativity_votes', 'content_votes']

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Project` instance exists
        before going any further.
        """
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})       