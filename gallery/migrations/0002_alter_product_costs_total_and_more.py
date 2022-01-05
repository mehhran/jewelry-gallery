# Generated by Django 4.0 on 2022-01-04 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='costs_total',
            field=models.DecimalField(decimal_places=2, help_text='Total costs (Stone setting, Plating, and Losses)', max_digits=19, verbose_name='Other Costs (Total)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='metal_fineness',
            field=models.IntegerField(help_text='0 < X =< 1000'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_base',
            field=models.DecimalField(decimal_places=3, help_text='Enter the base metal weight in grams', max_digits=7, verbose_name='base metal weight'),
        ),
        migrations.AlterField(
            model_name='profitgain',
            name='amount',
            field=models.IntegerField(help_text='0 =< X =< 100'),
        ),
    ]
