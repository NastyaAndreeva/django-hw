from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Note
from .forms import NoteForm

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'note_detail.html', {'note': note})

def create_or_edit_note(request, note_id=None):
    note = get_object_or_404(Note, id=note_id) if note_id else None

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'note_form.html', {'form': form, 'note': note})

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('note_list')

def index(request):
    return HttpResponse("Hello from Notes app")

def notes(request):
    return render(request, "notes.html")
