# Generated by Django 4.0 on 2021-12-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_order_isdelivered_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerdetails',
            options={'verbose_name_plural': 'Order Details'},
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=100),
        ),
    ]
