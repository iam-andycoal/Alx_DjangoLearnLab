from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
