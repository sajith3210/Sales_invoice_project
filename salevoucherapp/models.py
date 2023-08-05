from django.db import models

# Create your models here.

class addproduct(models.Model):
    product_name=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    rate=models.IntegerField(null=True,blank=True)
    amount=models.IntegerField( null=True,blank=True)
    gst=models.IntegerField(null=True,blank=True)
    total_amount=models.IntegerField(null=True,blank=True)

class invoice(models.Model):
    add_prod_id=models.ForeignKey(addproduct,on_delete=models.CASCADE,null=True,blank=True)
    bill_number=models.IntegerField(null=True,blank=True)
    product_name=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    rate=models.IntegerField(null=True,blank=True)
    amount=models.IntegerField( null=True,blank=True)
    gst=models.IntegerField(null=True,blank=True)
    total_amount=models.IntegerField(null=True,blank=True)