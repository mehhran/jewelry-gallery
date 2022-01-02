from django.db import models

import decimal

from gallery.managers import PriceManager, ProductManager, ProfitGainManager


def my_default():
    '''
    I'm using this default value for JSONField
    because the empty dict {} will raise Error
    in this version of Django.
    '''
    return {'': ''}


class Product(models.Model):
    METAL_TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('silver', 'Silver'),
    ]
    
    pid = models.IntegerField(verbose_name="product id", help_text="Enter the Barcode")
    name = models.CharField(max_length=100)
    
    metal_type = models.CharField(max_length=10, choices=METAL_TYPE_CHOICES)
    metal_fineness = models.IntegerField(help_text="0 < X =< 1000")
    
    weight_total = models.DecimalField(max_digits=7, decimal_places=3,
                                        verbose_name="total product weight",
                                        help_text="Enter the total weight (base metal + stones) in grams")
    
    weight_base = models.DecimalField(max_digits=7, decimal_places=3,
                                        verbose_name="base metal weight",
                                        help_text="Enter the base metal weight in grams")
    
    base_craft_fee = models.DecimalField(max_digits=19, decimal_places=2,
                                        help_text="Total craft fee for base")
    costs_total = models.DecimalField(max_digits=19, decimal_places=2,
                                        verbose_name= "Other Costs (Total)",
                                        help_text="Total costs (Stone setting, Plating, and Losses)")
    
    group = models.CharField(max_length=100, default="Other")

    data = models.JSONField(verbose_name="Extra Data", default=my_default)

    objects = ProductManager()

    def get_price(self):
        
        # getting the latest recorded price for the base metal
        try:
            if self.metal_type == "gold":
                base_metal_latest = Price.objects.get_latest("gold")
            elif self.metal_type == "platinum":
                base_metal_latest = Price.objects.get_latest("platinum")
            elif self.metal_type == "silver":
                base_metal_latest = Price.objects.get_latest("silver")
            
            assert isinstance(base_metal_latest.amount, decimal.Decimal)

            # converting the price to match the metal fineness
            base_metal_price = base_metal_latest.amount * self.metal_fineness / 1000

            # converting the price to be 'per gram' (if it isn't already)
            if base_metal_latest.basis == 'oz':
                base_metal_price /= decimal.Decimal(28.3495)
            elif base_metal_latest.basis == 'kg':
                base_metal_price /= 1000
            else:
                assert base_metal_latest.basis == 'g'

        except Exception as err:
            return err
        
        # adding up the prices of all stones associated with this product 
        try:
            stones_price_total = 0
            for stone in self.stone_set.all():
                stones_price_total += stone.price
        
        except Exception as err:
            return err
        
        try:
            profit_percentage = ProfitGain.objects.get_latest(self.group).amount
            
            assert isinstance(profit_percentage, int)
        
        except Exception as err:
            return err
        
        try:
            prime_cost = (self.weight_base * base_metal_price
                        + self.base_craft_fee 
                        + self.costs_total
                        + stones_price_total)

            price = prime_cost * decimal.Decimal(1 + profit_percentage/100)

        except Exception as err:
            return err
                
        return int(price)

    def __str__(self):
        return self.name + " - Barcode: " + str(self.pid)


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

    data = models.JSONField(verbose_name="Extra Data", default=my_default)

    def __str__(self):
        return self.name + str(" (count: %d)" % self.count)


class Price(models.Model):
    '''
    Used for storing prices of raw metals
    '''
    SORT_CHOICES = [
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('silver', 'Silver'),
    ]
    BASIS_CHOICES = [
        ('g', 'One Gram'),
        ('oz', 'One Ounce'),
        ('kg', 'One Kilogram')
    ]

    sort = models.CharField(max_length=10, choices=SORT_CHOICES)

    datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=19, decimal_places=2,
                                help_text="Enter the amount in USD")
    
    basis = models.CharField(max_length=10, choices=BASIS_CHOICES)

    data = models.JSONField(verbose_name="Extra Data", default=my_default)

    objects = PriceManager()

    def __str__(self):
        return (str(self.basis) + ' ' +
                str(self.sort) + ': ' +
                str(self.amount) + ' ' +
                str("$") + ' - ' +
                str(self.datetime.strftime('%m-%d-%Y %H:%M:%S')))


class ProfitGain(models.Model):
    '''
    To determine the desired profit gain percentage for a group of products
    '''
    product_group = models.CharField(max_length=100)

    amount = models.IntegerField(help_text="0 =< X =< 100")

    datetime = models.DateTimeField()

    objects = ProfitGainManager()

    class Meta:
        verbose_name = "Profit Gain Percentage"
        
    def __str__(self):
        return str("The amount of %d percent for the group '%s'"
                    % (self.amount, self.product_group))