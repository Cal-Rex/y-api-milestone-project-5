from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
                upload_to='images/', default=''
            )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_created']

        def __str__(self):
            return f"post no: {self.id} - {self.title}"