from django.db import models

# Create your models here.
# promotion - product 

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # products
    

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory =models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
       ('MEMBERSHIP_BRONZE', 'Bronze'),
       ('MEMBERSHIP_SILVER', 'Silver'),
       ('MEMBERSHIP_GOLD', 'Gold'),
    ]
    given_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    memership = models.CharField(max_length=255, choices=MEMBERSHIP_CHOICES, default='MEMBERSHIP_BRONZE')
   
    


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
     ('PAYMENT_STATUS_PENDING', 'Pending'),
     ('PAYMENT_STATUS_COMPLETE', 'Complete'),
     ('PAYMENT_STATUS_FAILED', 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=255, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )    
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderItem(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.PROTECT)    
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)    

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

   
   