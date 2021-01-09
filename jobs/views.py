from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'test.html')


def index2(request):
    return render(request, 'test2.html')

