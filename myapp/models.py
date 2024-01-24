from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    cat_name = models.CharField(max_length=65)

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcat_name

class Product(models.Model):
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_name = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to="productImg")

class Cart(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()

class Order(models.Model):
    name = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    products = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    terms_condition = models.BooleanField(default=False)