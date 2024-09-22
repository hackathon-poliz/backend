from rest_framework import serializers

from product.models import ProductProposal, ProductDemand, ProductUnit, Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = Product
        fields = "__all__"


class ProductUnitSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = ProductUnit
        fields = "__all__"


class ProductDemandSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = ProductDemand
        fields = "__all__"


class ProductProposalSerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        model = ProductProposal
        fields = "__all__"
