"""
database model for
likes
"""
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    db model fields
    """
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_by'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='liked_post'
    )

    class Meta:
        """
        Meta fields to allow only 1 like
        object per post per user
        default ordering by date created
        """
        ordering = ['-date_created']
        constraints = [
            UniqueConstraint(
                fields=['owner', 'post'],
                name='unique_like'
            )
        ]

    def __str__(self):
        return f"{self.owner} liked {self.post}"
