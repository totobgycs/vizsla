from django.db import models


class Codes(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return '{r.code}: {r.name}'.format(r=self)

    class Meta:
        abstract = True


class Issuer(Codes):

    class Meta:
        db_table = 'coincatalog\".\"issuer'

class Mint(Codes):

    class Meta:
        db_table = 'coincatalog\".\"mint'

class RulingAuthority(Codes):

    class Meta:
        db_table = 'coincatalog\".\"ruling_authority'

class Currency(Codes):

    class Meta:
        db_table = 'coincatalog\".\"currency'
        
