from django.db import models
from django.utils import timezone



SECTIONS = (
    ('hotnews', 'HotNews'),
    ('articles', 'Articles'),
    ('events', 'Events'),
    ('tech', 'Technologies'),
    ('politics', 'Politics'),
    ('culture', 'Culture'),
    ('sport', 'Sport'),
    ('economics', 'Economics'),
    ('incidents', 'Incidents'),
    ('travel', 'Travel'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    section = models.CharField(max_length=200, null=True, choices=SECTIONS)
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
