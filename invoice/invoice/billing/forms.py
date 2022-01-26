from cProfile import label
from django.contrib.auth.models import User
from django.forms import forms, widgets
from .models import *
import json

class DateInput (forms.DateInput):
    input_type = 'date'

class UserLoginForm (forms.ModelForm):
    class Meta:
        models = Client
        fields = ['username', 'password']

class ClientForm (forms.ModelForm):
    class Meta:
        models = Client
        fields = ['client_name', 'address1', 'province', 'contry', 'post_no', 'mobile_no',  'email_address', 'date_reated', 'uniqiId', 'last_updated']

class ProductForm (forms.ModelForm):
    class Meta:
        models = Products
        fields = ['title', 'description', 'quantity', 'price', 'curency', 'client_name', 'date_reated', 'uniqiId', 'last_updated']

class InvoiceForm (forms.ModelForm):
    dueDate = forms.DateField(
        required = True,
        label='Invoice Due',
        widget=DateInput(attrs={'class': 'form-control'})
    )
    models = Invoice
    fields = ['title', 'number', 'due_date', 'payment_terms', 'status', 'note', 'date_reated', 'uniqiId', 'last_updated']

class SettingForm (forms.ModelForm):
    class Meta:
        models = Settings
        fields = ['client_name', 'address1', 'province', 'contry', 'post_no', 'mobile_no',  'email_address', 'date_reated', 'uniqiId', 'last_updated']
