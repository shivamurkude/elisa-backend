from django.db import models
import uuid

class Registration(models.Model):
    SESSION_CHOICES = [
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('dance', 'Dance'),
        ('games', 'Games'),
    ]

    registration_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    session = models.CharField(max_length=20, choices=SESSION_CHOICES,blank=True, null=True)

    def __str__(self):
        return self.full_name
