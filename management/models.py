
from django.db import models
from django.utils.translation import gettext_lazy as _

class Farmer(models.Model):
    """ """
    name = models.CharField(verbose_name=_("Name"), max_length=20, unique=True)
    account_id = models.CharField(verbose_name=_("Telegram account id"), max_length=20, unique=True)
    tin = models.CharField(verbose_name=_("TIN"), unique=True, max_length=20)
    created_at = models.DateTimeField(verbose_name=_("Created Time"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated Time"), auto_now=True)

    class Meta:
        ordering = ["-id"]
        abstract = True
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name