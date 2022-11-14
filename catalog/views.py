from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Количество посещений этого представления, подсчитанное в переменной сеанса.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_best_books = Book.objects.filter(title__icontains='Best').count()

    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    context = {
                  'num_books': num_books,
                  'num_instances': num_instances,
                  'num_instances_available': num_instances_available,
                  'num_authors': num_authors,
                  'num_genre': num_genre,
                  'num_best_books': num_best_books,
                  'num_visits': num_visits,
              }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
