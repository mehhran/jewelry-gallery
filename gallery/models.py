from django.db import models

class Product(models.Model):
    METAL_TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('silver', 'Silver'),
    ]
    
    pid = models.IntegerField(verbose_name="product id", help_text="Enter the Barcode")
    name = models.CharField(max_length=100)
    
    metal_type = models.CharField(max_length=100, choices=METAL_TYPE_CHOICES)
    metal_fineness = models.IntegerField(help_text="0 < x =< 1000")
    
    weight_total = models.DecimalField(max_digits=7, decimal_places=3,
                                        verbose_name="total product weight",
                                        help_text="Enter the total weight (base metal + stones) in grams")
    
    weight_base = models.DecimalField(max_digits=7, decimal_places=3,
                                        verbose_name="base metal weight")
    
    base_craft_fee = models.DecimalField(max_digits=19, decimal_places=2,
                                        help_text="Total craft fee for base")
    costs_total = models.DecimalField(max_digits=19, decimal_places=2,
                                        help_text="Total costs (Stone setting, Plating, and Losses)")
    
    group = models.CharField(max_length=100)


class Stone(models.Model):
    '''
    Could represent one stone or a set of stones of one type/name.
    '''
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    
    price = models.DecimalField(max_digits=19, decimal_places=2)
    
    weight = models.DecimalField(max_digits=7, decimal_places=2,
                                help_text="Enter the weight in carats")    # A metric “carat” is defined as 200 milligrams
    color = models.CharField(max_length=100, blank=True)
    cut = models.CharField(max_length=100, blank=True)
    clarity = models.CharField(max_length=100, blank=True)

class Price(models.Model):
    pass

class ProfitGain(models.Model):
    pass