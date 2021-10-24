import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import UserModels


class ServiceTests(APITestCase):

    def setUp(self):
        UserModels.objects.create(name='Test')
        UserModels.objects.create(name='TesstTS')
        UserModels.objects.create(name='kubernetes')

    def test_list(self):
        url = reverse('repolist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0], {'pk': 1, 'name': 'Test', 'repository': []})
        self.assertEqual(UserModels.objects.get(pk=2).name, 'TesstTS')

    def tests_create(self):
        data = json.dumps({"name": "AbramtsevFV"})
        response = self.client.generic('GET', reverse('addrepo'), data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('name'), "AbramtsevFV")



    def test_update(self):
        data = json.dumps({"name": "kubernetes", "repository": [{
            "pk": 8,
            "repo": ".github",
            "read_me": "ReadME",
            "created": "2020-08-07T11:50:55Z"
        }]})
        response = self.client.generic('PATCH', reverse("repo_detail", args='2'), data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('repository'), [{'pk': 1, 'repo': '.github', 'read_me': 'ReadME', 'created': '2020-08-07T11:50:55Z'}])

    def test_delete(self):
        response = self.client.generic('DELETE', reverse("repo_detail", args='2'),  content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


