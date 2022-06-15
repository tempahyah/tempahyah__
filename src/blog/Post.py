from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField(max_length=5000, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="created date")
    published_date = models.DateTimeField(auto_now=True, verbose_name="published date")

    def __str__(self):
        return self.title


