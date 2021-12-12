# Generated by Django 4.0 on 2021-12-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customerdetails_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('package', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customerdetails',
            options={'verbose_name_plural': 'Customer Details'},
        ),
    ]