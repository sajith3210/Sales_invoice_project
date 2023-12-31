# Generated by Django 3.1.5 on 2023-08-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salevoucherapp', '0003_auto_20230802_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='gst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='product_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
