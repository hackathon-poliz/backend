from rest_framework import serializers

from place.models import Region, Area, Planted


class RegionSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Region
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Area
        fields = "__all__"


class PlantedSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Planted
        fields = "__all__"