from django.db import models
import datetime
class Register(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 500)

class Category(models.Model):
    def __str__(self):
        return self.name
    name= models.CharField(max_length = 100)

class Product(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default = 1)
    description = models.CharField(max_length = 200)
    image= models.ImageField(upload_to='pics')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)
   
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

class Order(models.Model):
    def __str__(self):
        return self.address
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Register,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length = 1000,default = 0000000000000000)
    phone = models.CharField(max_length = 10,default = 0000000000)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default = False)

class Details(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    orders = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    
class Testimonials(models.Model):
    def __str__(self):
        return self.customername
    customername = models.CharField(max_length = 500)
    review = models.CharField(max_length = 1000)