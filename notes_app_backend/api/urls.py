from django.urls import path
from .views import (
    health,
    NoteListCreateView,
    NoteRetrieveUpdateDestroyView,
)

app_name = "api"

urlpatterns = [
    path('health/', health, name='Health'),
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
]
