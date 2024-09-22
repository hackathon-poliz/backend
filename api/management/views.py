from rest_framework import viewsets

from api.management.serializer import AccountSerializer, FarmerSerializer, ProviderSerializer
from management.models import Account, Farmer, Provider


class AccountViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Farmer.objects.all()
    serializer_class =FarmerSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer