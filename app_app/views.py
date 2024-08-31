from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h2>Hello to you. welcome to a simple django app</h2>')
