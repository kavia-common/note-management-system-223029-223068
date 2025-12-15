from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Note
from .serializers import NoteSerializer


# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """
    Health check endpoint.

    Returns:
        200 OK with {"status": "ok"} payload to indicate the API is running.
    """
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


class NoteListCreateView(generics.ListCreateAPIView):
    """
    List all notes or create a new note.
    GET -> list notes
    POST -> create a note
    """
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update (PUT/PATCH), or delete a note by id.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
