from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
# Create your views here.
def landing(request):
    return render(request,'landing.html')

def note(request):
    notes = Note.objects.all()

    context = {
        'notes':notes
    }
    print(context)
    return render(request,'note_list.html',context)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer