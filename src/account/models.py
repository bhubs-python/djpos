from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    comment = models.TextField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.first_name) + "-" + str(self.last_name)


class Customer(Employee):
    pass



class Supplier(Employee):
    company_name = models.CharField(max_length=100, null=True, blank=True)



class Item(models.Model):
    barcode = models.CharField(max_length=100, null=True, blank=True)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    catagory = models.CharField(max_length=100, null=True, blank=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    wholesale_price = models.FloatField(null=True, blank=True)
    retail_price = models.FloatField(null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)

    quantity_stock = models.IntegerField(null=True, blank=True)
    receiving_quantity = models.IntegerField(null=True, blank=True)

    description = models.TextField(max_length=1000, null=True, blank=True)

    image = models.ImageField(upload_to='item/', default='no-img.jpg', null=True, blank=True)

    item_has_serial_number = models.BooleanField(default=False)
    reorder_level = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return str(self.barcode)
