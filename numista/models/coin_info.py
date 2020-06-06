from django.db.models import Q
from django.db.models import CheckConstraint
from django.contrib.postgres.fields import JSONField
from django.db import models

from .coin_info_manager import CoinInfoManager


class CoinInfo(models.Model):
    """
    Model for keeping Numista coin info in a local cache
    """

    numistaId = models.IntegerField(unique=True)
    lastDownload = models.DateTimeField(auto_now=True)
    numistaCoin = JSONField()
    numistaIssues = JSONField(null=True)

    def __str__(self):
        return '{r.numistaId}: {r.numistaCoin[title]}'.format(r=self)

    class Meta:
        db_table = 'numista\".\"coin_info'
