from django.db import models

# Create your models here.
class Country(models.Model):
    # country{code*	string
    #     Unique ID of the country on Numista
    # name*	string
    #     Name of the country}
    numista_country_id = models.CharField(max_length=30, unique=True)
    numista_country_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.numista_country_id + ': ' + self.numista_country_name

    class Meta:
        db_table = 'numista\".\"country'