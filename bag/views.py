from django.shortcuts import render, redirect, reverse

# Create your views here.

def shopping_bag(request):
    """A view returning the shopping bag page"""
    
    return render(request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add item/items in the shopping bag based on quantity and redirect to same page """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Edit the shopping bag items and redirect to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))
