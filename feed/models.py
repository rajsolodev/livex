from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:50]

    @property
    def display_user(self):
        """Returns the username or 'Guest' if no user is linked."""
        if self.user:
            return self.user.username
        return "Guest"