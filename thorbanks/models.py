from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Transaction(models.Model):
    STATUS_PENDING = 'P'
    STATUS_FAILED = 'F'
    STATUS_COMPLETED = 'C'
    STATUS_CHOICES = (
        (STATUS_PENDING, _('pending')),
        (STATUS_FAILED, _('failed')),
        (STATUS_COMPLETED, _('completed')),
    )

    bank_name = models.CharField(_("bank"), max_length=16)
    description = models.CharField(_("reference description"), max_length=255, help_text=_("reference description"))
    amount = models.FloatField(_("amount"))
    currency = models.CharField(_("currency"), max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(_("status"), max_length=1, default=STATUS_PENDING, choices=STATUS_CHOICES)
    redirect_after_success = models.CharField(max_length=255, editable=False)
    redirect_on_failure = models.CharField(max_length=255, editable=False)

    def __str__(self):
        return "Transaction %s - %s %.2f from %s [%s]" % \
               (self.id, self.currency, self.amount, self.bank_name, self.get_status_display())

    class Meta:
        verbose_name = _("transaction")
        ordering = ['-last_modified']
