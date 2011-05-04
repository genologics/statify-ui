from django.db import models

class Entry(models.Model):
    guid = models.CharField(max_length=255)
    entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Registration(models.Model):
    guid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)