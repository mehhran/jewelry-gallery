# Generated by Django 4.0 on 2021-12-26 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(help_text='Enter the Barcode', verbose_name='product id')),
                ('name', models.CharField(max_length=100)),
                ('metal_type', models.CharField(choices=[('gold', 'Gold'), ('platinum', 'Platinum'), ('silver', 'Silver')], max_length=100)),
                ('metal_fineness', models.IntegerField(help_text='0 < x =< 1000')),
                ('weight_total', models.DecimalField(decimal_places=3, help_text='Enter the total weight (base metal + stones) in grams', max_digits=7, verbose_name='total product weight')),
                ('weight_base', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='base metal weight')),
                ('base_craft_fee', models.DecimalField(decimal_places=2, help_text='Total craft fee for base', max_digits=19)),
                ('group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfitGain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('weight', models.DecimalField(decimal_places=2, help_text='Enter the weight in carats', max_digits=7)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('cut', models.CharField(blank=True, max_length=100)),
                ('clarity', models.CharField(blank=True, max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.product')),
            ],
        ),
    ]