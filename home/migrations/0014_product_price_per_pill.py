# Generated by Django 4.0 on 2021-12-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_customerdetails_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_per_pill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
