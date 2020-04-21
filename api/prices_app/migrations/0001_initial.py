# Generated by Django 3.0.5 on 2020-04-19 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('eshop_url', models.CharField(max_length=100)),
                ('currency_code', models.CharField(max_length=3)),
                ('currency_symbol', models.CharField(blank=True, max_length=5, null=True)),
                ('currency_usd_conversion', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_value', models.FloatField(blank=True, null=True)),
                ('usd_value', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prices_app.Country')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prices_app.Game')),
            ],
            options={
                'db_table': 'listing',
            },
        ),
    ]
