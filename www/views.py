from django.shortcuts import render

# Create your views here.

def www(request):
    return render(request, 'index.html', {})
