from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

    tbr = Book.objects.filter(read=False, started_date=None).values()
    read = Book.objects.filter(read=True).values()
    current = Book.objects.filter(~Q(started_date=None), read=False).values()
    return render(request, 'books/index.html', {'tbr': tbr, 'read': read, 'current': current, 'form': form})
