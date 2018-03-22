from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    priority = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title