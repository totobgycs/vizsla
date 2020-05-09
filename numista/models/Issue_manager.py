from django.db import models

from numista.models.coin import Coin
from numista.services.numista import NumistaClient

import json
from flatten_json import flatten


class IssueManager(models.Manager):
    def get_from_json(self, coin_numista_id: str, issue_json_arr: [dict]):
        """
        Creates a Coin model entit from a json (dict).
        Parameters
        ----------
            coin_json (json): json descrioption of coin as returned by Numista
        """
        for issue_json in issue_json_arr:
            coin, _ = Coin.objects.get_or_create(numistaId=coin_numista_id)
            result = self.model(
                coin=coin,
                numistaId=issue_json['id']
            )

            flat_obj = flatten(issue_json)
            for f in self.model._meta.get_fields():
                if f.name == 'id':
                    pass
                elif (f.name in flat_obj) and (getattr(result, f.name) in f.empty_values):
                    setattr(result, f.name, flat_obj[f.name])
                elif hasattr(f, 'json_id') and (f.json_id in flat_obj) and (getattr(result, f.name) in f.empty_values):
                    setattr(result, f.name, flat_obj[f.json_id])
            yield result
