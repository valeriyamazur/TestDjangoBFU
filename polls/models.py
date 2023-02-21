from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Book(models.Model):
    author = models.CharField(max_length=200)
    book_name = models.CharField(max_length=200)
    date_published = models.IntegerField()

    def __str__(self):
        return self.book_name

    class Meta:
        ordering = ["book_name", "author"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book_detail', args=[str(self.id)])


class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    book = models.ForeignKey(Book, null=True, on_delete=models.DO_NOTHING)
    date_published = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = "comment"
