# Generated by Django 4.0.1 on 2022-01-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=40, null=True)),
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
    ]
