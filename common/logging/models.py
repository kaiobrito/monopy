from django.db import models

class EventType(models.IntegerChoices):
    LOG = 0, "Log"

class Event(models.Model):
    name = models.CharField(max_length=255)
    event_type = models.IntegerField(choices=EventType.choices)

    def __str__(self) -> str:
        return self.name