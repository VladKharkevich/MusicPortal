from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)
