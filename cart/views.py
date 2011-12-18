# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from ecomstore.cart import cart
from django.core.context_processors import csrf

from django.http import HttpResponseRedirect
from ecomstore.checkout import checkout
from ecomstore import settings

def show_cart(request, template_name="cart/cart.html"):
    #update the csrf token
    c = {}
    c.update(csrf(request))

    if request.method =='POST':

        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
        if postdata['submit'] == 'Checkout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
#    cart_item_count = cart.cart_item_count(request)
    
    page_title = 'Shopping Cart'
    #for google checkout button
    merchant_id = settings.GOOGLE_CHECKOUT_MERCHANT_ID
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
