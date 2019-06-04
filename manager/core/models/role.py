import uuid

from django.db import models


class Role(models.Model):
    class Meta:
        db_table = 'role'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=200)
    salary = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "{0} - R${1}".format(self.name, self.salary)
