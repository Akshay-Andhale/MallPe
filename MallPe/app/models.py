from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES = (
('Andaman and Nicobar','Andaman and Nicobar'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal','Arunachal'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chandigarh','Chandigarh'),
('Chhattisgarh','Chhattisgarh'),
('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Delhi','Delhi'),
('Goa','Goa')
)

class Customer(models.Model):
    user_customer = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100,choices=STATE_CHOICES)

    def __str__(self):
        return str(self.id)



CATEGORY_CHOICES = (
('M','Mobile'),
('L','Laptop'),
('TW','Top wear'),
('BW','Bottom wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES)
    product_image = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user_cart = models.ForeignKey(User,on_delete=models.CASCADE)
    product_cart = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product_cart.discounted_price



STATUS_CHOICES = (
('Accepted','Accepted'),
('Packed','Packed'),
('On the way','On the way'),
('Delivered','Delivered'),
('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user_OrderPlaced = models.ForeignKey(User,on_delete=models.CASCADE)
    customer_OrderPlaced = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_OrderPlaced = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending')
    
    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product_OrderPlaced.discounted_price