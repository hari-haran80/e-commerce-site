# Generated by Django 4.2.7 on 2024-06-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0014_alter_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
