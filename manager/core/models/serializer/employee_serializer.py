from rest_framework import serializers

from ...models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        exclude = ('id',)
        depth = 2
        allow_null = False
