from django.db import models

# Create your models here.


class Coin(models.Model):
    # coin
    #     id*	            integer         Unique ID of the coin on Numista
    #     url     	        string          URL to the coin on Numista
    #     title*	        string          Title of the coin
    #     country	        country         Ref
    #     minYear	        integer         First year the coin was minted (in the Gregorian calendar)
    #     maxYear	        integer         Last year the coin was minted (in the Gregorian calendar)
    #     type	            string          Type of coin
    #     value_text	    string          Face value in text format
    #     value_currency    currency        Ref
    #     shape	            string          Shape of coin
    #     composition       string          Composition of coin (metallic content)
    #     weight	        number($float)  Weight of the coin
    #     size	            number($float)  Size of coin (diameter)
    #     thickness	        number($float)  Thickness of the coin
    #     obverse_picture	string          URL to the picture of the side of the coin
    #     obverse_thumbnail	string          URL to the thumbnail of the picture of the side of the coin
    #     reverse_picture	string          URL to the picture of the side of the coin
    #     reverse_thumbnail	string          URL to the thumbnail of the picture of the side of the coin
    numistaId = models.IntegerField(unique=True)
    numistaId.json_id = 'id'
    url = models.TextField()
    title = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    minYear = models.IntegerField(null=True)
    maxYear = models.IntegerField(null=True)
    coinType = models.CharField(max_length=200)
    coinType.json_id = 'type'
    value_text = models.CharField(max_length=200)
    value_currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    shape = models.CharField(max_length=200)
    composition_text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    size = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    thickness = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    obverse_picture = models.TextField()
    obverse_thumbnail = models.TextField()
    reverse_picture = models.TextField()
    reverse_thumbnail = models.TextField()

    def __str__(self):
        return '{r.numistaId}: {r.title}'.format(r=self)

    class Meta:
        db_table = 'numista\".\"coin'
