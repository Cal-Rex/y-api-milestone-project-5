"""
database model for
votes
"""
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from comments.models import Comment


class Vote(models.Model):
    """
    db model fields
    """
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vote_owner")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="parent_comment")

    class Meta:
        """
        Meta fields to allow only 1 vote
        object per comment per user
        default ordering by date created
        """
        ordering = ['-date_created']
        constraints = [
            UniqueConstraint(
                fields=['owner', 'comment'],
                name='unique_vote'
            )
        ]

    def __str__(self):
        return f"{self.owner} voted for comment {self.comment}"
