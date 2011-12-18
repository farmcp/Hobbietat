from ecomstore.checkout import google_checkout

#change this code if you change the 3rd party processor
def get_checkout_url(request):
    return google_checkout.get_checkout_url(request)
