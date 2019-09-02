from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """ View cart items """
    return render(request, 'cart.html')

def add_to_cart(request):
    """ Add items to cart """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('all_products'))

def adjust_cart(request):
    """ Adjust the quantity of an item in the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))