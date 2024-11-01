from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_books_wise = Book.objects.filter(title__icontains=('Wise')).count()

    print(Book.objects.filter(title__icontains='Wise'))
    num_instances = BookInstance.objects.all().count()
    num_genres_fiction = Book.objects.filter(genre__name='Fiction').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_books_wise': num_books_wise,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres_fiction
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)