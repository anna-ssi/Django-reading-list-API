from django import forms
from .utils.scraper import url_scraper

from .models import Book


class BookCreateForm(forms.ModelForm):
    url = forms.CharField(max_length=250)

    class Meta:
        model = Book
        exclude = ('title', 'description', 'author', 'rating', 'rating_count', 'review_count', 'page')

    def save(self, commit=True):
        data = url_scraper(self.cleaned_data['url'])
        Book().create(data)
        return self
