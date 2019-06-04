from rest_framework import serializers

from ...models.role_history import RoleHistory


class RoleHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleHistory
        fields = '__all__'
