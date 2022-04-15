from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Topic(models.Model):
    """New topic creating by the user."""
    # CharField - keeping small data like name / country / town / title
    # max_length - how much space should be keep for this information
    text = models.CharField(max_length=200)
    # take current date from moment when the user write data
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Model representation as a string."""
        return self.text


class Entry(models.Model):
    """Specific information about progress in learning any topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Model representation as a string."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
