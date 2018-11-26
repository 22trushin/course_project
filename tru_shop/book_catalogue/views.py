from django.shortcuts import render

from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from book_catalogue.models import BooksCatalogue

# Create your views here.


def view(request):
    if request.method == 'GET':
        books = BooksCatalogue.objects.all()
        return render(request, 'book_catalogue/index.html', {'books': books})
    return HttpResponse(status=405)