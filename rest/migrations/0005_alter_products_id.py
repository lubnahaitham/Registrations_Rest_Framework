# Generated by Django 3.2.9 on 2022-01-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_alter_seller_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
