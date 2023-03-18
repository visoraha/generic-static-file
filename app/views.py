from django.shortcuts import render

# Create your views here.
def imageset(request):
    return render(request,'imageset.html')
