"""
database model for
profiles
"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    db model fields
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
                upload_to='images/',
                default='../media/images/y-big-canvas-white_dtobjd.png'
            )
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        """
        default ordering by date created
        """
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.owner}'s profile"


# parameters `sender` and `**kwargs` removed
def create_profile(sender, instance, created, **kwargs):
    """
    signal to create a profile record
    for a user when a user is created
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
