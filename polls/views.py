from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from django.views import generic, View
from django.db.models import Q 
from .forms import CommentForm
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
    comment_form = CommentForm
    template_name = 'polls/comment_detail.html'
    def get(self, request, pk):
        name = Book.objects.filter(id=pk)
        book_name, author = '', ''
        for n in name:
            book_name, author = n.book_name, n.author
            
        user = auth.get_user(request)
        form = self.comment_form
        comments = Comment.objects.all()
        comments = Comment.objects.filter(book=pk)
        return render(request, self.template_name, {'comments': comments, 'name':  book_name, 'author' : author, 'form': form})
        
        
def add_comment(request, pk):
    error = ''
    form = CommentForm(request.POST)
    #comment = get_object_or_404(Comment, book=pk)
    if form.is_valid():
        form.user = auth.get_user(request)
        form.book = pk
        form.comment = comment.cleaned_data['comment_area']
        form.save()
        #return redirect ('login/')
    else:
        error = 'Лошара'

    return render(request, 'polls/comment_detail.html', {'form': form, 'error' : error})
    
    

