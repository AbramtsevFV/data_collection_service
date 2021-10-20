from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import UserModels, RepoModels


class RepoSerializer(ModelSerializer):
    class Meta:
        model = RepoModels
        fields = ('pk', 'repo', 'read_me', 'created')


class UserSerialezr(WritableNestedModelSerializer):
    repository = RepoSerializer(many=True)

    class Meta:
        model = UserModels
        fields = ('pk', 'name', 'repository')
