from django.shortcuts import render

# Create your views here.

def products(request):
    """A view returning the index page"""
    
    return render(request, 'products/products.html')