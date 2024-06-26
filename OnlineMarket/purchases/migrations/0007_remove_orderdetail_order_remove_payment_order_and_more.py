# Generated by Django 5.0.2 on 2024-04-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0006_order_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='Product',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]
