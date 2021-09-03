from django.shortcuts import render
from django.views.generic import ListView
from .forms import Search

from service.models import *

class User_List(ListView):
    paginate_by = 10
    model = UserModels
    queryset = UserModels.objects.all()
    template_name = 'web_interface/index.html'
    form_class = Search()



class Repo_list(ListView):
    model = RepoModels
    template_name = 'web_interface/repo.html'


    def get(self, request, pk):
        queryset = RepoModels.objects.filter(name_id=pk).values()
        return render(request, self.template_name,{'repo_list':queryset}, )







