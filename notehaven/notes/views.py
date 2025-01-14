from django.shortcuts import render
from .models import Note
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