import uuid

from django.db import models


class Address(models.Model):

    class Meta:
        db_table = 'address'
        verbose_name_plural = 'adresses'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(null=False, blank=False, max_length=200)
    number = models.IntegerField(null=False, blank=False)
    neighborhood = models.CharField(null=False, blank=False, max_length=200)
    additional_information = models.CharField(null=True, blank=True, max_length=200)
    zip_code = models.IntegerField(null=False, blank=False)
    city = models.ForeignKey('city', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %s" % (self.street, self.neighborhood, self.city)
