from django.db import models


class ProductCategory(models.Model):
    """ """
    title = models.CharField(verbose_name="Title", max_length=100)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    """ """
    name = models.CharField(verbose_name="Name", max_length=50)
    category = models.ForeignKey(verbose_name="Category", to="ProductCategory", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductUnit(models.Model):
    """ """
    quantity = models.IntegerField(verbose_name="Seedlings quantity")
    weight = models.DecimalField(verbose_name="Volume", max_length=4, max_digits=2)

    class Meta:
        verbose_name = "Product unit"
        verbose_name_plural = "Product units"


class ProductDemand(models.Model):
    """ """
    weight = models.DecimalField(verbose_name="Volume", max_length=4, max_digits=2)
    provider = models.ForeignKey(verbose_name="Provider", to="management.Provider", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product demand"
        verbose_name_plural = "Product demands"


class ProductProposal(models.Model):
    """ """
    demand = models.ForeignKey(verbose_name="Demand", to="ProductDemand", on_delete=models.CASCADE)
    weight = models.DecimalField(verbose_name="Volume", max_length=4, max_digits=2)
    price = models.DecimalField(verbose_name="Price", max_length=8, max_digits=2)

    class Meta:
        verbose_name = "Product proposal"
        verbose_name_plural = "Product proposals"
