import uuid

from django.db import models
from ..validators.validate_cpf import validate_cpf


class Person(models.Model):
    class Meta:
        db_table = 'person'
        verbose_name_plural = 'people'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False, max_length=100)
    cpf = models.CharField(null=False, blank=False, max_length=11, unique=True, validators=[validate_cpf])
    birthday = models.DateField(null=False, blank=False)
    address = models.ForeignKey('address', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.cpf)
