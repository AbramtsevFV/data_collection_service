from django.urls import path
from .views import User_List, Repo_list


urlpatterns = [
    path('', User_List.as_view(), name='home'),
    path('repo_list/<int:pk>', Repo_list.as_view(), name='repo_list')
]