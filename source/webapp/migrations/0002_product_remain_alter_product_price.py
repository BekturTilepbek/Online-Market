# Generated by Django 5.0.6 on 2024-07-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remain',
            field=models.PositiveIntegerField(null=True, verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
    ]
