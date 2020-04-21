from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "John Smith"
    }))
    street_address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "1234 Main St"})
    )
    country = CountryField(blank_label="(select country)").formfield(
        widget=CountrySelectWidget(attrs={"class": "custom-select d-block w-100"})
    )
    state = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "TX"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "City"}))
    zip = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
