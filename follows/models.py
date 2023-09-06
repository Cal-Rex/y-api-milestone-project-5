"""
database model for
follows
"""
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User


class Follow(models.Model):
    """
    db model fields
    """
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
    )

    class Meta:
        """
        Meta fields to allow only 1 follow
        object per following user
        per followed user
        default ordering by date created
        """
        ordering = ['-date_created']
        constraints = [
            UniqueConstraint(
                fields=['owner', 'followed'],
                name='unique_follow'
            )
        ]

    def __str__(self):
        return f"follow: {self.followed}"
