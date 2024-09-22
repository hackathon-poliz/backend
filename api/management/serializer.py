from rest_framework import serializers

from management.models import Account, Farmer, Provider


class AccountSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Account
        fields = "__all__"


class FarmerSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Farmer
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Provider
        fields = "__all__"