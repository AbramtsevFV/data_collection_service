from django.contrib import admin
from .models import UserModels, RepoModels


admin.site.register(UserModels)
admin.site.register(RepoModels)

