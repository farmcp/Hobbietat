from ecomstore.checkout import google_checkout
from ecomstore.cart import cart
from ecomstore.checkout.models import Order, OrderItem
from ecomstore.checkout.forms import CheckoutForm
from ecomstore.checkout import authnet
from ecomstore import settings
#from django.core import urlresolvers
from django.core import urlresolvers
import urllib
import ecomstore.checkout

#change this code if you change the 3rd party processor
def get_checkout_url(request):
    #return google_checkout.get_checkout_url(request)
     print urlresolvers.reverse('checkout')
     return urlresolvers.reverse('checkout')

def process(request):
    #Transaction results
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'
    
    #get the data from the post request
    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number','')
    exp_month = postdata.get('credit_card_expire_month','')
    exp_year = postdata.get('credit_card_expire_year','')
    exp_date = exp_month + exp_year
    cvv = postdata.get('credit_card_cvv','')
    amount = cart.cart_subtotal(request)

    #get data about the customer
    b_name = postdata.get('billing_name','')
    b_address = postdata.get('billing_address1','')
    b_city = postdata.get('billing_city','')
    b_state = postdata.get('billing_state','')
    b_zip = postdata.get('billing_zip','')
    b_country = postdata.get('billing_country','')
    u_email = postdata.get('email','')
    u_phone = postdata.get('phone','')
    s_name = postdata.get('shipping_name','')
    s_address = postdata.get('shipping_address1','')
    s_city = postdata.get('shipping_city','')
    s_state = postdata.get('shipping_state','')
    s_zip = postdata.get('shipping_zip','')
    s_country = postdata.get('shipping_country','')

    results = {}

    #capture the data and send to authorize.net
    response = authnet.do_auth_capture(amount=amount,
                                       card_num=card_num,
                                       exp_date=exp_date,
                                       card_cvv=cvv,
                                       bill_name=b_name,
                                       bill_address=b_address,
                                       bill_city=b_city,
                                       bill_state=b_state,
                                       bill_zip=b_zip,
                                       bill_country=b_country,
                                       email = u_email,
                                       phone = u_phone,
                                       ship_name = s_name,
                                       ship_address = s_address,
                                       ship_city = s_city,
                                       ship_state = s_state,
                                       ship_zip=s_zip,
                                       ship_country = s_country)
    if response[0] == APPROVED:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number':order.id, 'message':''}
    if response[0] == DECLINED:
        results = {'order_number':0,'message':'There is a problem with your credit card.'}
    if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
        results = {'order_number':0,'message':'Error processing your order.'}
    print results
    print response[0]
    return results

def create_order(request, transaction_id):
    order=Order()
    checkout_form = CheckoutForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    #link to user account
    if request.user.is_authenticated():
         order.user = request.user

    order.status = Order.SUBMITTED
    order.save()
    
    #if the order save succeeded
    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            #create order item for each cart item
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()
        #all set, empty cart
        cart.empty_cart(request)
    
    #save profile infor for future orders
    if request.user.is_authenticated():
         from ecomstore.accounts import profile
         profile.set(request)
    
    #return the new order object
    return order
