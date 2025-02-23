# Generated by Django 5.1.6 on 2025-02-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
