from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from django.views import generic, View
from django.db.models import Q
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.template.context_processors import csrf


class BookListView(generic.ListView):
    model = Book


class Comments(generic.ListView):
    model = Comment


def get_queryset(request):
    query = request.GET.get('q')
    object_list = Book.objects.filter(
        Q(book_name__iregex=query) | Q(author__iregex=query)
    )
    return render(request, 'polls/search.html', {'object_list': object_list})


class GetComment(generic.DetailView):
    model = Comment
    template_name = 'polls/comment_detail.html'

    def get(self, request, pk):
        name = Book.objects.get(id=pk)
        user = request.user
        comments = Comment.objects.filter(book=pk)
        return render(request, self.template_name,
                      {'comments': comments, 'user': user, "book_name": name,})


def add_comment(request, book, user):

    if request.method == 'POST':
        print('_____________________________--')
        Comment.objects.create(
            comment=request.POST.get('comment'),
            book=Book.objects.get(id=book),
            user=User.objects.get(id=user),
        )

        return redirect('book_detail', pk= book)



def del_comm(request, book, comment):
    Comment.objects.filter(id=comment).delete()
    return redirect('book_detail', pk=book)