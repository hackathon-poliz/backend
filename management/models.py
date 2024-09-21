from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class Account(models.Model):
    phone = models.CharField(verbose_name="Phone Number", max_length=13)
    otp = models.CharField(verbose_name="One time password")
    otp_exp = models.DateTimeField(verbose_name="Otp Exp")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class Farmer(models.Model):
    """ """
    account = models.OneToOneField(verbose_name="Account", to="Account", on_delete=models.CASCADE)


    class Meta:
        ordering = ["-id"]
        verbose_name = _("Farmer")
        verbose_name_plural = _("Farmers")

    def __str__(self):
        return self.account.__str__()


class Provider(models.Model):
    """ """
    account = models.OneToOneField(verbose_name="Account", to="Account", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")

    def __str__(self):
        return self.account.__str__()



