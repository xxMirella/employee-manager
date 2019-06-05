from rest_framework import serializers

from ...models.state import State


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'
        allow_null = False
