from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    return render(request, 'myapp/current_datetime.html', {'now': now})