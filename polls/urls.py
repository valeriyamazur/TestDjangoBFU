from . import views
from django.urls import include, re_path, path

urlpatterns = [
    path('home/', views.BookListView.as_view(), name='home'),
    path('', views.BookListView.as_view(), name='home_'),
    path('home/<str:pk>', views.GetComment.as_view(), name='book_detail'),
    path('comments/', views.Comments.as_view(), name='comments'),
    path('search/', views.get_queryset, name='search'),
    path('add-comment/<str:book>/<str:user>/', views.add_comment, name='book'),
    path('del-comment/<str:book>/<str:comment>/', views.del_comm, name='book_del_com'),

]
