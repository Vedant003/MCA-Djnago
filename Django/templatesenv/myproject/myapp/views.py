from django.shortcuts import render

def hello(request):
    context = {
        'name': 'Vedant',
        'age': 21,
    }
    return render(request, 'myapp/hello.html', context)
