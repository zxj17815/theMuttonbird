from django import forms
from . import models

class BookForm(forms.Form):
    name = forms.CharField(max_length=10)
    # publisher_id = forms.IntegerField(widget=forms.Select)
    publish_date = forms.DateField()