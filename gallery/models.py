from django.db import models

from gallery.managers import PriceManager


def my_default():
    '''
    I'm using this default value because the empty dict {} for JSONField
    will raise Error in this version of Django.
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
    
    group = models.CharField(max_length=100, default="Other")

    data = models.JSONField(verbose_name="Extra Data", default=my_default)


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

    amount = models.IntegerField(help_text="E.g.: The amount of 15 will add 15 percent of the product's prime cost")

    datetime = models.DateTimeField()

    class Meta:
        verbose_name = "Profit Gain Percentage"
        
    def __str__(self):
        return str("The amount of %s percent for the '%s'group - %s"
        % (self.amount, self.product_group, self.datetime.strftime('%m-%d-%Y %H:%M:%S')))