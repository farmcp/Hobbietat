from django.contrib import admin
from ecomstore.catalog.models import Product, Category, FishingStyle, Shape, Materials
from ecomstore.catalog.forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'old_price','date_created', 'date_updated','quantity','size','sku',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-date_created']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_desc']
    #exclude=('date_created', 'date_updated',)
    
    #set up slug to be generated from product name
    prepopulated_fields= {'slug':('sku',)}

#register the product model with the admin site
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'date_created', 'date_updated',)
    list_display_links=('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields=['name','description','meta_keywords', 'meta_description']
    #exclude= ('date_created', 'date_updated',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ShapeAdmin(admin.ModelAdmin):
    list_display=('name', 'description',)
    list_display_links=('name',)
    list_per_page=10
    ordering=['name']
    search_fields=['name', 'description']
admin.site.register(Shape, ShapeAdmin)

class MaterialsAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_display_links=('name',)
    list_per_page=10
    ordering=['name']
admin.site.register(Materials, MaterialsAdmin)

class FishingStyleAdmin(admin.ModelAdmin):
    list_display=('style',)
    list_display_links=('style',)
    list_per_page=10
    ordering=['style']
admin.site.register(FishingStyle, FishingStyleAdmin)    
