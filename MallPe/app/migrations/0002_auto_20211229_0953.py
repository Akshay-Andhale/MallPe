# Generated by Django 3.2.8 on 2021-12-29 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_cart',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user_cart',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user_customer',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='customer_OrderPlaced',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='product_OrderPlaced',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='user_OrderPlaced',
            new_name='user',
        ),
    ]
