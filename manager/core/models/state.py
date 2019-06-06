import uuid

from django.db import models


class State(models.Model):

    class Meta:
        db_table = 'state'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=200)
    country = models.ForeignKey('country', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.country)
