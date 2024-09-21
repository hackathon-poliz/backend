from django.db import models

from management.choices import RoleChoice


class Account(models.Model):
    phone = models.CharField(verbose_name="Phone Number", max_length=13)
    first_name = models.CharField(verbose_name="First name", max_length=15)
    last_name = models.CharField(verbose_name="Last name", max_length=15)
    otp = models.CharField(verbose_name="One time password")
    otp_exp = models.DateTimeField(verbose_name="Otp Exp")
    role = models.PositiveSmallIntegerField(verbose_name="Role", choices=RoleChoice.choices)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        name = self.get_full_name()
        return self.phone if name == " " else name

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Farmer(models.Model):
    """ """
    account = models.OneToOneField(verbose_name="Account", to="Account", on_delete=models.CASCADE)


    class Meta:
        ordering = ["-id"]
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"

    def __str__(self):
        return self.account.__str__()


class Provider(models.Model):
    """ """
    account = models.OneToOneField(verbose_name="Account", to="Account", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.account.__str__()



