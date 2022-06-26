from django.shortcuts import render

# Create your views here.

def bag(request):
    """A view returning the index page"""
    
    return render(request, 'bag/shopping_bag.html')