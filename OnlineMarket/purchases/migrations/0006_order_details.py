# Generated by Django 5.0.2 on 2024-04-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_category'),
        ('purchases', '0005_remove_orderdetail_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='details',
            field=models.ManyToManyField(through='purchases.OrderDetail', to='product.product'),
        ),
    ]
