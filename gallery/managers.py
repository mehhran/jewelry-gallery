from django.db import models

class PriceManager(models.Manager):
    
    def get_latest(self, sort, **kwargs):
        try:
            prices = self.get_queryset().filter(sort=sort)
            if 'basis' in kwargs:
                prices = prices.filter(basis=kwargs['basis'])
            latest = prices[len(prices)-1]
            return latest
        except:
            return str("It seems like there is no price recorded for %s." % sort)