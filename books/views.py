from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from elasticsearch_dsl.query import MultiMatch

from .documents import BookDocument
from .forms import BookCreateForm
from .models import Book


@csrf_exempt
def home(request):
    form = BookCreateForm()
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
        return redirect('/book')

    data = Book.objects.all().values()
    return render(request, 'books/index.html', {'data': data, 'form': form})


def search(request):
    q = request.GET.get('q')

    if q:
        posts = BookDocument.search().query(MultiMatch(query=q, fields=['title', 'description', 'author']))
    else:
        posts = ''

    return render(request, 'search/search.html', {'posts': posts})
