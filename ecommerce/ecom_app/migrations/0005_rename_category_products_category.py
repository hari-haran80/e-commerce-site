# Generated by Django 4.2.7 on 2024-05-26 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_category_products_delete_head_phone_delete_laptop_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Category',
            new_name='category',
        ),
    ]
