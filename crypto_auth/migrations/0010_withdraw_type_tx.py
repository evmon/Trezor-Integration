# Generated by Django 2.1.5 on 2019-01-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_auth', '0009_auto_20190108_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='type_tx',
            field=models.CharField(blank=True, choices=[('Credit', 'CREDIT'), ('Debit', 'DEBIT'), ('Fee', 'FEE')], help_text='Type of transaction', max_length=10),
        ),
    ]
