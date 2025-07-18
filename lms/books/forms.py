from zoneinfo import available_timezones
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields =['title','author','isbn','published_date','is_available']