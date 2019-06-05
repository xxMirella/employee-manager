from rest_framework import serializers

from ...models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1
        allow_null = False
