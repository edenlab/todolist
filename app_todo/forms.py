from django import forms
from django.forms import widgets

class DateRangeForm(forms.Form):
    start_date = forms.DateTimeField(widget=forms.DateInput)
    end_date = forms.DateTimeField(widget=forms.DateInput)


