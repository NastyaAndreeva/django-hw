from django.shortcuts import HttpResponse, render
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def index(request):
    return HttpResponse("Hello from Notes app")

def notes(request):
    return render(request, "notes.html")
