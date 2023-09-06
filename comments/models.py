"""
database model for
Comment
"""
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    db model
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='parent_post')
    content = models.TextField(blank=False)

    class Meta:
        """
        Meta fields to
        default ordering by date created
        """
        ordering = ['-date_created']

    def __str__(self):
        return f"comment no: {self.id} for {self.post.title}"
