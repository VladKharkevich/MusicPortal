from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
