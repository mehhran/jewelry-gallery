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
            return str("It seems like there is no price record for %s." % sort)


class ProfitGainManager(models.Manager):
    
    def get_latest(self, product_group):
        try:
            percentages = self.get_queryset().filter(product_group=product_group)
            last_percentage = percentages[len(percentages)-1]
            return last_percentage
        except:
            return str("It seems like there is no Profit-Gain-Percentage record for the group %s." % product_group)


class ProductManager(models.Manager):
    
    def product_price_dic(self):
        """
            Returns a dictionary of product:price pairs.
        """
        all_products = self.model.objects.all()
        return {p.id : p.get_price() for p in all_products}
    
    def product_image_link_dic(self):
        """
            Returns a dictionary of product:image_link pairs.
        """
        all_products = self.model.objects.all()
        return {p.id : p.get_image_link() for p in all_products}
