from django.db import models


class Region(models.Model):
    """ """
    name = models.CharField(verbose_name="Name", max_length=50)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Area(models.Model):
    """ """
    name = models.CharField(verbose_name="Name", max_length=50)
    is_free = models.BooleanField(verbose_name="Is free", default=False)
    region = models.ForeignKey(verbose_name="Region", to="Region", on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(verbose_name="Latitude", default=0, max_digits=20, decimal_places=18)
    longitude = models.DecimalField(verbose_name="Longitude", default=0, max_digits=21, decimal_places=18)


    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"


class Planted(models.Model):
    area = models.ForeignKey(verbose_name="Area", to="Area", on_delete=models.CASCADE)
    square = models.FloatField(verbose_name="Square")
    percent = models.PositiveSmallIntegerField(verbose_name="Square percent")
    product = models.ForeignKey(verbose_name="Product", to="product.Product", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Planted"
        verbose_name_plural = "Planted"