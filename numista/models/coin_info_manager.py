from typing import Dict, Tuple, NewType
from django.db import models
from vizsla import settings
from numista.services.numista import NumistaClient
from datetime import date

NumistaId=NewType('NumistaId', int)

class CoinInfoManager(models.Manager):
    """
    Model manager for CoinInfo models
    """

    def get_from_numista_id(self, numista_id: NumistaId) -> Tuple[Dict, Dict]:
        """
        Return information get from numista.com for the coinspecified by the parameter.
        Parameters
        ----------
            numista_id : numista id of coin to be created. 
        Returns
        -------
            resulting json of the coin and issues api call
        """
        numistaClient = NumistaClient()
        return numistaClient.get_coin(numista_id), numistaClient.get_coin_issues(numista_id)

    def get_or_retrive(self, numista_id: NumistaId) -> Tuple[Dict, Dict]:
        """
        Return coin and issue information got from cache database, or queried from numista.com
        Parameters
        ----------
            numista_id : numista id of coin to be created. 
        Returns
        -------
            jsons of the coin and issues 
        """

        try:
            coin_info = self.model.get(numistaId=numista_id)
            if (date.today - coin_info.lastDownload).days < settings.NUMISTA_REFRESH_DAYS:
                return coin_info.numistaCoin, coin_info.numistaIssues
        except self.model.DoesNotExist:
            pass

        numista_coin, numista_issues = self.get_from_numista_id(numista_id)
        self.model.update_or_create(
            numistaId=numista_id,
            defaults={
                'numistaCoin': numista_coin,
                'numistaIssues': numista_issues
            }
        )
        return numista_coin, numista_issues
