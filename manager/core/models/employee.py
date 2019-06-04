import uuid

from django.db import models


class Employee(models.Model):
    class Meta:
        db_table = 'employee'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('person', on_delete=models.CASCADE)
    role = models.ForeignKey('role', on_delete=models.CASCADE)
    hiring_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.person.name, self.role.name, self.hiring_date)
