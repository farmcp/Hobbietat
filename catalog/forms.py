from django import forms
from ecomstore.catalog.models import Product
from django.shortcuts import get_object_or_404
from django.forms.fields import ChoiceField
from django.forms.widgets import Select

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
    
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than $0.00')
        return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
    #this is the product form - quantity is where a customer enters the number of items they want to buy
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity', 'maxlength':'5'}), error_messages={'invalid':'Please enter a valid quantity.'}, min_value =1)
    
    product_slug = forms.CharField(widget=forms.HiddenInput())

    #need to include what size SelectDateWidget the user can request
#    sizes_available = []
#    sizes_available.append((7,7))
#    sizes_available.append((9,9))


    #get all the products with the specified name that is being requested
#    all_products = Product.objects.all()
 
    #for the products that have quantity > 1 and size = x
#    for p in all_products:
#        if p.quantity > 0:
            #
    #add a <select> for the form
#    pick_size = forms.ChoiceField(widget=forms.Select, choices=sizes_available)
    
    #override the default __init__ so we can see the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    #custom validation to check for cookies
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data
