# Generated by Django 4.0 on 2021-12-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_product_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='extra',
            field=models.IntegerField(default=0),
        ),
    ]