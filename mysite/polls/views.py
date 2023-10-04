from django.shortcuts import HttpResponse, render


def index(request):
    # return render(request, "home.html")
    return HttpResponse("Hello from Notes app")
