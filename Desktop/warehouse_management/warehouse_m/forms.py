from django import forms
from .models import Product


class PaginateOrAll(forms.Form):
    show = forms.ModelChoiceField(queryset=['PAGINATE', 'ALL PRODUCTS'])


