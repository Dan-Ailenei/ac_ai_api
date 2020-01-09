from django.shortcuts import render


def index(request):
    return render(request, 'nlp/index.html', {})
