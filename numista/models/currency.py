from django.db import models

# Create your models here.
class Currency(models.Model):
    # currency{
    # id*	integer
    #       Unique ID of the currency on Numista
    # name*	string
    #       Name of the currency}
    numistaId = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{r.numistaId}: {r.name}'.format(r=self)

    class Meta:
        db_table = 'numista\".\"currency'

