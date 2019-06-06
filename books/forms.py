from django import forms

from .models import Book


class BookCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    started_date = forms.DateTimeField(required=False,
                                       widget=forms.widgets.DateTimeInput(attrs={'type': 'date', "autoclose": True}))
    finished_date = forms.DateTimeField(required=False,
                                        widget=forms.widgets.DateTimeInput(attrs={'type': 'date', "autoclose": True}))
    rating = forms.IntegerField(required=False)
    review = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Book
        fields = ('title', 'started_date', 'finished_date', 'rating', 'review')

    def save(self, commit=True):
        book = super(BookCreateForm, self).save(commit=True)
        book.title = self.cleaned_data['title']
        book.started_date = self.cleaned_data['started_date']
        book.finished_date = self.cleaned_data['finished_date']
        book.rating = self.cleaned_data['rating']
        book.review = self.cleaned_data['review']

        if book.finished_date:
            book.read = True
            print(book.read)

        if commit:
            book.save()

        return book
