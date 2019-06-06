import uuid

from django.db import models


class RoleHistory(models.Model):
    class Meta:
        db_table = 'role_history'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('person', on_delete=models.CASCADE)
    role = models.ForeignKey('role', on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
    additional_information = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.person.name, self.role.name, self.date)
