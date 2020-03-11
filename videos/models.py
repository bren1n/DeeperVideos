from django.db import models
from django.utils import timezone

class Video(models.Model):
    THEME_CHOICES = (
        ('Music', 'Music'),
        ('Gaming', 'Gaming'),
        ('Vlog', 'Vlog'),
        ('Review', 'Review'),
        ('Tutorial', 'Tutorial'),
        ('Educational', 'Educational'),
        ('For kids', 'For kids'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    theme = models.CharField(max_length=200, choices=THEME_CHOICES)
    publish_date = models.DateField(default=timezone.now)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    