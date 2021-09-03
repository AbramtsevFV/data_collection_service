from django.urls import path
from .views import RepoViews, AddRepo

repo_list =  RepoViews.as_view({'get': 'list',})
repo_detail = RepoViews.as_view(
    {
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)
repo_create = RepoViews.as_view({'post': 'create'})

urlpatterns = [
    path('repo_list/', repo_list, name='repolist'),
    path('repo_create/', repo_create, name='repo_create'),
    path('repo_detail/<int:pk>', repo_detail, name='repo_detail'),
    path('addrepo/', AddRepo.as_view(), name='addrepo'),
]