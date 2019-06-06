import uuid

from django.db import models


class Country(models.Model):

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'counties'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=200)

    def __str__(self):
        return self.name
