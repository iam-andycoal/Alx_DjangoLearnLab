from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    class BookViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD for Book model.
    Only admin users can create, update, or delete.
    Any authenticated user can view/list books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # use a permission class or classes
    # One option: require IsAuthenticated for all, then further check per action
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

