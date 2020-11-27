from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    noun = models.CharField(max_length=10)
    verb = models.CharField(max_length=10)
    timespent = models.IntegerField()
    properties = JSONField()
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'


class Rule(models.Model):
    name = models.CharField(max_length=100)
    noun = models.CharField(max_length=10, blank=True,null=True)
    count = models.IntegerField(blank=True, null=True)
    timeframe = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    total_value = models.FloatField(blank=True, null=True)
