# Generated by Django 4.0.1 on 2022-01-26 11:45

import billing.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=40, null=True)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, choices=[('Kabul', 'Kabul'), ('Paktika', 'Paktika'), ('Ghazni', 'Ghazni')], max_length=100, null=True)),
                ('contry', models.CharField(blank=True, choices=[('Afghanistan', 'Afghanistan'), ('India', 'India'), ('Pakistan', 'Pakistan')], max_length=100, null=True)),
                ('post_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=100, null=True)),
                ('uniqiId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('date_reated', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='client',
            old_name='clientName',
            new_name='client_name',
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('curency', models.FloatField(blank=True, choices=[('AF', 'AFN'), ('$', 'USD'), ('RS', 'PKR')], default='AF', max_length=100, null=True)),
                ('uniqiId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('date_reated', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='billing.client')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('payment_terms', models.CharField(blank=True, choices=[('14 Days', '14 Days'), ('30 Days', '30 Days'), ('60 Days', '60 Days')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('CURRENT', 'CURRENT'), ('CANCELED', 'CANCELED'), ('UNPAID', 'UNPAID'), ('PAID', 'PAID'), ('OVERDUE', 'OVERDUE'), ('MARKED FROAD', 'MARKED FROAD')], default='UNPAID', max_length=50, null=True)),
                ('note', models.TextField(blank=True, max_length=200, null=True, verbose_name=billing.models.Client)),
                ('uniqiId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('date_reated', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.products')),
            ],
        ),
    ]
