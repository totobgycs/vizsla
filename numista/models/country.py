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

