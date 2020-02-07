from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    product_description=models.CharField(max_length=300)
    published_date=models.DateField()
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    phoneNumber=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=300,default='')


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    phoneNumber=models.CharField(max_length=50)
    address_line_1=models.CharField(max_length=150)
    address_line_2=models.CharField(max_length=150)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    zip_code=models.CharField(max_length=30)

    # def __str__(self):
    #     return self.order_id

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:7]+'.....'