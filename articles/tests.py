from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article


class ArticleTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com"
        )
        self.title = "This is a test title"
        self.body = "This is a test body"
        self.article = Article.objects.create(
            title=self.title, body=self.body, author=self.user
        )

    def test_string_representation(self):
        article = Article(title="This is a test title")
        self.assertEqual(str(article), article.title)
        self.assertEqual(str(article), article.title)
        self.assertEqual(str(article), article.title)

    
