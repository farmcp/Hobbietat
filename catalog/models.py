from django.db import models
#from PIL import Image
# Create your models here.

##
#create categories for each of the products. each will have a name a description and some other properties.
#categoies can consist of - heads, skirts, onshore lures, onshore skirts, onshore heads, deep sea hooks, shore hooks, line, etc.
##
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma delimited SEO keywords.')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Description used for SEO.')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering=['-date_created']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    #this permalink will return a slug (self.slug) as a url to the url.py regex that references it. in this case category_slug will use self.slug to insert into the url regex
    @models.permalink
    def get_absolute_url(self):
        return('catalog_category',(), {'category_slug':self.slug})
    

#create a table class for the shapes that a product can have
class Shape(models.Model):
    name = models.CharField(max_length=255, unique = True)
    description=models.CharField(max_length=255)
    class Meta:
        db_table='product_shapes'
        ordering=['name']

    def __unicode__(self):
        return self.name
    

class Materials(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table='materials'
        ordering=['name']
    def __unicode__(self):
        return self.name

class FishingStyle(models.Model):
    style=models.CharField(max_length=255, unique=True)
    class Meta:
        db_table='style'
        ordering=['style']
    def __unicode__(self):
        return self.style



class Product(models.Model):
    name = models.CharField(max_length=255, unique = True)
    slug = models.SlugField(max_length=255, unique = True, help_text='unique value for product page url, created by name.')
    brand = models.CharField(max_length=255)
    sku=models.CharField(max_length=255)
    
    #price that the product will be set at
    price=models.DecimalField(max_digits=9, decimal_places=2)
    
    #old price can have a blank field because it doesn't need to have a value
    old_price=models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    
#remove this since we are changing the image    image=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/products/main')
    thumbnail = models.ImageField(upload_to='images/products/thumbnails')
    image_caption = models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    is_bestseller=models.BooleanField(default=False)
    is_featured=models.BooleanField(default=False)
    quantity=models.IntegerField()
    description=models.TextField()
    meta_keywords=models.CharField(max_length=255, help_text='comma separated values for SEO.')
    meta_desc=models.CharField(max_length=255, help_text='description for SEO.')

    #add date created and updated fields
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField(Category)
    

    ##additional properties for Hobbietat site
    size = models.DecimalField(max_digits=9, decimal_places=2)
    colors = models.CharField(max_length=255)
    best_used_with=models.CharField(max_length=255) #might need to think if you can put other products here
    manufacturer = models.CharField(max_length=255)

    #define other relationships for hobbietat
    shape = models.ManyToManyField(Shape)
    materials = models.ManyToManyField(Materials)
    style = models.ManyToManyField(FishingStyle)
    
    class Meta:
        db_table='products'
        ordering = ['-date_created']
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return('catalog_product',(),{'product_slug':self.slug})
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
    
    
