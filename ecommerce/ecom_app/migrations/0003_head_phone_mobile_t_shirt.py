# Generated by Django 4.2.7 on 2024-02-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_remove_laptop_productname_alter_laptop_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Head_phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeadphoneName', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Images', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MobileName', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Images', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='T_shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_shirt', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Images', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
