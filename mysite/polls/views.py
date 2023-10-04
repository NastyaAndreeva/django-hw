from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("Hello from Notes app")

def notes(request):
    return render(request, "notes.html")
