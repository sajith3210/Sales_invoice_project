# Generated by Django 3.1.5 on 2023-08-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salevoucherapp', '0002_invoice_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='gst',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.IntegerField(),
        ),
    ]