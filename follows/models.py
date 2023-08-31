from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from profiles.models import Profile


class Follow(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        ordering = ['-date_created']
        constraints = [
            UniqueConstraint(
                fields=['owner', 'followed'],
                name='unique_follow'
            )
        ]

        def __str__(self):
            return f"{self.owner} now following {self.followed}"
