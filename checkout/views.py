from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from ecomstore.checkout.forms import CheckoutForm
from ecomstore.checkout.models import Order, OrderItem
from ecomstore.checkout import checkout
from ecomstore.cart import cart
from django.core.context_processors import csrf
from ecomstore.accounts import profile


# Create your views here.
def show_checkout(request, template_name='checkout/checkout.html'):
    c = {}
    c.update(csrf(request))
    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            #process the credit card with the data that's posted to the server - billing information
            response = checkout.process(request)
            order_number = response.get('order_number',0)
            print 'this is the order number: ' + str(order_number)
            error_message = response.get('message','')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('checkout_receipt')
                print request.session['order_number']
                return HttpResponseRedirect(receipt_url)
        else:
            error_message='Correct the errors below'

    else:
        if request.user.is_authenticated():
            user_profile = profile.retrieve(request)
            form = CheckoutForm(instance=user_profile)
        else:
            form = CheckoutForm()
                
    page_title = 'Checkout'
    return render_to_response(template_name, locals(), context_instance= RequestContext(request))

def receipt(request, template_name='checkout/receipt.html'):
    order_number = request.session.get('order_number','')
    print 'this is receipt order number: ' + str(order_number)
    if order_number:
        print 'in order_number'
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        print 'not in order number'
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url) 
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
