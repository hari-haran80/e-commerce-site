# Generated by Django 4.2.7 on 2024-05-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0006_products_description_products_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
