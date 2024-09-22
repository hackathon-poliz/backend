from rest_framework import viewsets

from api.place.serializer import RegionSerializer, AreaSerializer, PlantedSerializer
from place.models import Region, Area, Planted


class RegionViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Region
    serializer_class = RegionSerializer



class AreaViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Area
    serializer_class = AreaSerializer



class PlantedViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Planted
    serializer_class = PlantedSerializer

