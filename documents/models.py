from django.db import models

# Create your models here.

class Document(models.Model):
    """Dummy document model, just for testing use"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
