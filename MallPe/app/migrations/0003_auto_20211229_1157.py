# Generated by Django 3.2.8 on 2021-12-29 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211229_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='product_cart',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_cart',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='user_customer',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='customer',
            new_name='customer_OrderPlaced',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='product',
            new_name='product_OrderPlaced',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='user',
            new_name='user_OrderPlaced',
        ),
    ]
