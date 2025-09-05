from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

views.register
from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', ...),  # existing views
    path('library/<int:pk>/', ...),  # existing views

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-area/', admin_view, name='admin_view'),
    path('librarian-area/', librarian_view, name='librarian_view'),
    path('member-area/', member_view, name='member_view'),
]

["add_book/", "edit_book/", "delete_book"]
