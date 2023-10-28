from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article, Comment


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
    
    def test_article_content(self):
        self.assertEqual(f"{self.article.title}", self.title)
        self.assertEqual(f"{self.article.body}", self.body)
        self.assertEqual(f"{self.article.author}", "testuser")

class CommentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com"
        )
        self.title = "This is a test title"
        self.body = "This is a test body"
        self.article = Article.objects.create(
            title=self.title, body=self.body, author=self.user
        )
        self.comment = Comment.objects.create(
            comment="This is a test comment", article=self.article, author=self.user
        )

    def test_string_representation(self):
        comment = Comment(comment="This is a test comment")
        self.assertEqual(str(comment), comment.comment)
        self.assertEqual(str(comment), comment.comment)
        self.assertEqual(str(comment), comment.comment)

    def test_comment_content(self):
        self.assertEqual(f"{self.comment.comment}", "This is a test comment")
        self.assertEqual(f"{self.comment.author}", "testuser")
        self.assertEqual(f"{self.comment.article}", self.title)

    

    
