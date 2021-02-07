from django.urls import reverse
from rest_framework.test import APITestCase
from home.models import Article, User


class ApiArticleTestCase(APITestCase):
    def setUp(self) -> None:
        self.article1 = Article.objects.create(
            title="Test title",
            content="test content"
        )

        self.article2 = Article.objects.create(
            title="Test2 title",
            content="test2 content"
        )

    def test_api_article_get(self):
        url = reverse('articles-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json['results'][0],
            {
                "title": "Test title",
                "id": 1,
                "content": "test content",
                "author": None,
                "link": 'http://testserver/api/articles/1/'
            },
        )

    def test_api_article_create(self):
        url = reverse('articles-list')
        response_json = self.client.get(url).json()
        self.assertEqual(response_json['count'], 2)

    def test_api_article_destroy(self):
        self.article1.delete()
        url = reverse('articles-list')
        response_json = self.client.get(url).json()
        self.assertEqual(response_json['count'], 1)

    def test_api_article_get_list(self):
        url = reverse('articles-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json['results'],
            [{
                "title": "Test title",
                "id": 1,
                "content": "test content",
                "author": None,
                "link": 'http://testserver/api/articles/1/'
            },
                {
                    "title": "Test2 title",
                    "id": 2,
                    "content": "test2 content",
                    "author": None,
                    "link": 'http://testserver/api/articles/2/'
                }]
        )

    def test_api_article_update(self):
        self.article1.title = 'Test-test title'
        self.article1.save()
        url = reverse('articles-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json['results'][0],
            {
                "title": "Test-test title",
                "id": 1,
                "content": "test content",
                "author": None,
                "link": 'http://testserver/api/articles/1/'
            })


class ApiUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="Test user",
        )

    def test_api_user_get(self):
        url = reverse('users-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json[0],
            {
                "username": "Test user",
                "first_name": "",
                "last_name": "",
                "id": 1,
                'profile': None,
                'articles': [],
                'link': 'http://testserver/api/users/Test%20user/'
            },
        )

    def test_api_user_create(self):
        url = reverse('users-list')
        response_json = self.client.get(url).json()
        self.assertEqual(len(response_json), 1)

    def test_api_user_delete(self):
        self.user.delete()
        url = reverse('users-list')
        response_json = self.client.get(url).json()
        self.assertEqual(len(response_json), 0)

    def test_api_user_get_list(self):
        url = reverse('users-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json,
            [{
                "username": "Test user",
                "first_name": "",
                "last_name": "",
                "id": 1,
                'profile': None,
                'articles': [],
                'link': 'http://testserver/api/users/Test%20user/'
            }]
        )

    def test_api_article_update(self):
        self.user.username = 'Test-test user'
        self.user.save()
        url = reverse('users-list')
        response_json = self.client.get(url).json()
        self.assertEqual(
            response_json[0],
            {
                "username": "Test-test user",
                "first_name": "",
                "last_name": "",
                "id": 1,
                'profile': None,
                'articles': [],
                'link': 'http://testserver/api/users/Test-test%20user/'
            })
