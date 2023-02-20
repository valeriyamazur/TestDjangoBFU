from . import views
from django.urls import include, re_path, path

urlpatterns = [
    path('home/', views.BookListView.as_view(), name='home'),
    path('', views.BookListView.as_view(), name='home_'),
    re_path(r'^home/(?P<pk>\d+)/$', views.GetComment.as_view(), name='book_detail'),
    path('comments/', views.Comments.as_view(), name='comments'),
    path('search/', views.get_queryset, name='search'),
    path('add-comment/<str:book>/<str:user>/', views.add_comment, name='book'),

]
