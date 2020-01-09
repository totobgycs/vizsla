from django.db import models

# Create your models here.
class Country(models.Model):
    # country{
    #   code*	string
    #         Unique ID of the country on Numista
    #   name*	string
    #         Name of the country}
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return '{r.code}: {r.name}'.format(r=self) 

    class Meta:
        db_table = 'numista\".\"country'

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

class Issue(models.Model):
    # issue{
    # id*	integer
    #         Unique ID of the issue on Numista
    # isDated	boolean
    #         Informs whether the issuance year is present on the coin
    # year	integer
    #         Issuance year as written on the coin, if the coin is dated
    # calendar	string
    #         Calendar in which the element 'year' is provided
    # gregorianYear	integer
    #         Issuance year in Gregorian calendat, if the coin is dated
    # minYear	integer
    #         First year of issuance in Gregorian calendar, if the coin is non dated
    # maxYear	integer
    #         Last year of issuance in Gregorian calendar, if the coin is non dated
    # mintLetter	string
    #         Mint letter
    # comment	string
    #         Comment about the issue}
    numistaId = models.IntegerField(unique=True)
    isDated = models.BooleanField()
    year = models.IntegerField()
    calendar = models.CharField(max_length=200)
    gregorianYear = models.IntegerField(null=True)
    minYear = models.IntegerField(null=True)
    maxYear = models.IntegerField(null=True)
    mintLetter = models.CharField(max_length=20)
    comment = models.TextField()

    def __str__(self):
        return '{r.numistaId}: {r.year}'.format(r=self)

    class Meta:
        db_table = 'numista\".\"issue'
