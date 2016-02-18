from django.db import models


class ContentInteractionLog(models.Model):
    """This Model provides a record of an interaction with a content item."""

    user = models.IntegerField()  # Just so we can group logs, in reality might be a foreign key.
    start_timestamp = models.DateTimeField()
    completion_timestamp = models.DateTimeField()
