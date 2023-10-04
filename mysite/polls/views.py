from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("Hello from Notes app")

def home(request):
    return render(request, "home.html")
