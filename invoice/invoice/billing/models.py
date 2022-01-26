from audioop import reverse
import email
from itertools import product
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


from uuid import uuid4

# Create your models here.


class Client (models.Model):

    PROVINCES = [
        ('Kabul', 'Kabul'),
        ('Paktika', 'Paktika'),
        ('Ghazni', 'Ghazni'),
    ]
    COUNTRY = [
        ('Afghanistan', 'Afghanistan'),
        ('India', 'India'),
        ('Pakistan', 'Pakistan'),
    ]
    client_name = models.CharField(null=True, blank=True, max_length=40)
    address1 = models.CharField(null=True, blank=True, max_length=100)
    province = models.CharField(
        choices=PROVINCES, null=True, blank=True, max_length=100)
    contry = models.CharField(
        choices=COUNTRY, null=True, blank=True, max_length=100)
    post_no = models.CharField(null=True, blank=True, max_length=100)
    mobile_no = models.CharField(null=True, blank=True, max_length=15)
    email_address = models.EmailField(null=True, blank=True, max_length=100)

    uniqiId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=100)
    date_reated = models.DateTimeField(null=True,  blank=True, max_length=50)
    last_updated = models.DateTimeField(null=True,  blank=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.client_name, self.email_address, self.uniqiId)

    def get_absolute_url(self):
        return reverse('client-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_reated is None:
            self.date_reated = timezone.localtime(timezone.now())
        if self.uniqiId is None:
            self.uniqiId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)


class Products (models.Model):

    CURENCY = [
        ('AF', 'AFN'),
        ('$', 'USD'),
        ('RS', 'PKR'),
    ]

    title = models.CharField(null=True, blank=True, max_length=40)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.CharField(null=True, blank=True, max_length=100)
    curency = models.FloatField(
        null=True, blank=True, choices=CURENCY, default='AF', max_length=100)
    client_name = models.ForeignKey(
        Client, null=True, blank=True, on_delete=models.DO_NOTHING)

    uniqiId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=100)
    date_reated = models.DateTimeField(null=True,  blank=True, max_length=50)
    last_updated = models.DateTimeField(null=True,  blank=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.title, self.client_name, self.uniqiId)

    def get_absolute_url(self):
        return reverse('products-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_reated is None:
            self.date_reated = timezone.localtime(timezone.now())
        if self.uniqiId is None:
            self.uniqiId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.last_updated = timezone.localtime(timezone.now())

        super(Products, self).save(*args, **kwargs)


class Invoice (models.Model):

    TERMS = [
        ('14 Days', '14 Days'),
        ('30 Days', '30 Days'),
        ('60 Days', '60 Days'),
    ]
    STATUS = [
        ('CURRENT', 'CURRENT'),
        ('CANCELED', 'CANCELED'),
        ('UNPAID', 'UNPAID'),
        ('PAID', 'PAID'),
        ('OVERDUE', 'OVERDUE'),
        ('MARKED FROAD', 'MARKED FROAD'),
    ]

    title = models.CharField(null=True, blank=True, max_length=40)
    number = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(choices=TERMS, null=True,  blank=True,max_length=50)
    status = models.CharField(null=True, blank=True,
                              choices=STATUS, default='UNPAID', max_length=50)
    note = models.TextField(Client, null=True, blank=True, max_length=200)

    # related fields
    client = models.ForeignKey(
        Client, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Products, null=True, blank=True, on_delete=models.SET_NULL)

    uniqiId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=100)
    date_reated = models.DateTimeField(null=True,  blank=True, max_length=50)
    last_updated = models.DateTimeField(null=True,  blank=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.title, self.client_name, self.uniqiId)

    def get_absolute_url(self):
        return reverse('invoice-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_reated is None:
            self.date_reated = timezone.localtime(timezone.now())
        if self.uniqiId is None:
            self.uniqiId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


class Settings (models.Model):

    PROVINCES = [
        ('Kabul', 'Kabul'),
        ('Paktika', 'Paktika'),
        ('Ghazni', 'Ghazni'),
    ]
    COUNTRY = [
        ('Afghanistan', 'Afghanistan'),
        ('India', 'India'),
        ('Pakistan', 'Pakistan'),
    ]
    client_name = models.CharField(null=True, blank=True, max_length=40)
    address1 = models.CharField(null=True, blank=True, max_length=100)
    province = models.CharField(
        choices=PROVINCES, null=True, blank=True, max_length=100)
    contry = models.CharField(
        choices=COUNTRY, null=True, blank=True, max_length=100)
    post_no = models.CharField(null=True, blank=True, max_length=100)
    mobile_no = models.CharField(null=True, blank=True, max_length=15)
    email_address = models.EmailField(null=True, blank=True, max_length=100)

    uniqiId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=100)
    date_reated = models.DateTimeField(null=True,  blank=True, max_length=50)
    last_updated = models.DateTimeField(null=True,  blank=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.client_name, self.email_address, self.uniqiId)

    def get_absolute_url(self):
        return reverse('client-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_reated is None:
            self.date_reated = timezone.localtime(timezone.now())
        if self.uniqiId is None:
            self.uniqiId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.slug = slugify('{} {}'.format(self.client_name, self.uniqiId))

        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)
