from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hardware/index.html')

# Create your views here.
def niko(request):
    context = {'name': 'zoe'}
    return render(request, 'hardware/niko.html', context)
