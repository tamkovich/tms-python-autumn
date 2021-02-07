from django.test import TestCase, Client

from home.models import Article


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.article = Article.objects.create(
            title="Test title",
            content="test content"
        )
        self.client = Client()

    def test_create_article(self):
        self.assertEqual(Article.objects.count(), 1)

    def test_article_str(self):
        self.assertEqual(
            str(self.article),
            "Test title - test content"
        )

    def test_api_get_article(self):
        response_json = self.client.get('/api/articles/').json()
        self.assertEqual(response_json['count'], 1)
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
