from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def booth(request):
    return render(request, 'booth.html')

def notice(request):
    return render(request, 'notice.html')
