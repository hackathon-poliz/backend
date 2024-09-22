from rest_framework import viewsets

from api.product.serializer import ProductUnitSerializer, ProductDemandSerializer, ProductProposalSerializer, \
    ProductSerializer, ProductCategorySerializer
from product.models import ProductUnit, ProductDemand, ProductProposal, Product, ProductCategory


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """ """

    queryset = ProductCategory
    serializer_class = ProductCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ """

    queryset = Product
    serializer_class = ProductSerializer

class ProductUnitViewSet(viewsets.ModelViewSet):
    """ """

    queryset = ProductUnit
    serializer_class = ProductUnitSerializer

class ProductDemandViewSet(viewsets.ModelViewSet):
    """ """

    queryset = ProductDemand
    serializer_class = ProductDemandSerializer

class ProductProposalViewSet(viewsets.ModelViewSet):
    """ """

    queryset = ProductProposal
    serializer_class = ProductProposalSerializer