# Generated by Django 3.2.9 on 2022-01-12 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_alter_products_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seller',
            options={'ordering': ['-name']},
        ),
    ]
