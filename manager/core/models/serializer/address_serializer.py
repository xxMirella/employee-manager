from rest_framework import serializers

from ...models.address import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
