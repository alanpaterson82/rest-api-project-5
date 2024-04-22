from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    """
    Friend model, related to 'owner' and 'friended'.
    'owner' is a User that is following a User.
    'friended' is a User that is followed by 'owner'.
    We need the related_name attribute so that django can differentiate.
    between 'owner' and 'friended' who both are User model instances.
    'unique_together' makes sure a user can't 'double friend' the same user.
    """
    owner = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE
    )
    friended = models.ForeignKey(
        User, related_name='friended', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'friended']

    def __str__(self):
        return f'{self.owner} {self.friended}'