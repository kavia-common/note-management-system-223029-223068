from django.db import models


class Note(models.Model):
    """
    Note model representing a user note with title and content.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
