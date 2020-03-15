from django.db import models
from django.utils.timezone import now

# from core.models import User


class Kudo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    by_user = models.ForeignKey(
        'core.User', on_delete=models.CASCADE, related_name="kudos_given"
    )
    to_user = models.ForeignKey(
        'core.User', on_delete=models.CASCADE, related_name="kudos_received"
    )
    awarded = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ["-awarded"]

    def __str__(self):
        return self.title
