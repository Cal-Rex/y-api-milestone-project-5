"""
database model for
posts
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    db model fields
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
                upload_to='images/', default=''
            )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        """
        default ordering by date created
        """
        ordering = ['-date_created']

    def __str__(self):
        return f"post no: {self} - {self.title}"
