from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    bag = request.session.get('bag', {})

    if flavour:
        if item_id in list(bag.keys()):
            if flavour in bag[item_id]['items_by_flavour'].keys():
                bag[item_id]['items_by_flavour'][flavour] += quantity
            else:
                bag[item_id]['items_by_flavour'][flavour] = quantity
        else:
            bag[item_id] = {'items_by_flavour': {flavour: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adujusts the quantity of the specified products in the shopping cart """

    quantity = int(request.POST.get('quantity'))
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    bag = request.session.get('bag', {})

    if flavour:
        if quantity > 0:
            bag[item_id]['items_by_flavour'][flavour] = quantity
        else:
            del bag[item_id]['items_by_flavour'][flavour]
            if not bag[item_id]['items_by_flavour']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Removes the item from the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        flavour = None
        if 'product_flavour' in request.POST:
            flavour = request.POST['product_flavour']
        bag = request.session.get('bag', {})
        print(bag)

        if flavour:
            print(flavour)
            del bag[item_id]['items_by_flavour'][flavour]
            if not bag[item_id]['items_by_flavour']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)