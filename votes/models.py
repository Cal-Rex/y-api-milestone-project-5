from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']
        constraints = [
            UniqueConstraint(
                fields=['owner', 'comment'],
                name='unique_vote'
            )
        ]

    def __str__(self):
        return f"{self.owner} voted for comment {self.post.id}"