# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from ecomstore.catalog.models import Category, Product, Shape, Materials, FishingStyle
from django.template import RequestContext
from django.core import urlresolvers
from ecomstore.cart import cart
from django.http import HttpResponseRedirect
from ecomstore.catalog.forms import ProductAddToCartForm
from decimal import Decimal


def index(request, template_name="catalog/index.html"):
    page_title = "Hobbietat"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="catalog/category.html"):
    c= get_object_or_404(Category, slug=category_slug)
    #get all the products in the category then used in the category.html template
    products_4 = c.product_set.filter(size=4)
    products_5 = c.product_set.filter(size="5.38")
    products_7 = c.product_set.filter(size=7)
    products_9 = c.product_set.filter(size=9)
    products_12 = c.product_set.filter(size=12)
#    products = c.product_set.all() --> This calls all the products if you need to
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_product(request, product_slug, template_name='catalog/product.html'):
    print 'in show product'
    #get the product that is being shown
    p = get_object_or_404(Product, slug=product_slug)
#    categories = p.categories.filter(is_active=True)
    categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_desc
    current_p_sku = p.sku

    #need to evaluate the http method
    if request.method == 'POST':
        #add to cart
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            #if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        #its a GET, create the unbound form. Note request is a kwarg
        #This will create the form, label_suffix uses the : following the text
        form = ProductAddToCartForm(request=request, label_suffix=':  ')

    #assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    
    #set the test cookie on our first GET request
    request.session.set_test_cookie()
    return render_to_response("catalog/product.html", locals(), context_instance=RequestContext(request))

