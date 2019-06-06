from rest_framework import serializers

from ...models.role import Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        exclude = ('id',)
        allow_null = False
