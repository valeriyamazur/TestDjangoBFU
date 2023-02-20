from django.contrib import admin
from .models import Book, Comment


#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','author')

    
admin.site.register(Book, BookAdmin)


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'book' ,'date_published')
    list_filter = ('book',)
    search_fields = ("book__startswith", )



