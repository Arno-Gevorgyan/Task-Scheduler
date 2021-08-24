from django.db import models


class Event(models.Model):
    date = models.DateTimeField('datetime', blank=True, null=True)