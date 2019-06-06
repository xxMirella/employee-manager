import uuid

from django.db import models


class City(models.Model):

    class Meta:
        db_table = 'city'
        verbose_name_plural = 'cities'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=200)
    state = models.ForeignKey('state', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.state)
