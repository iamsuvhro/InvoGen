from django.db import models
# Create your models here.


class BillDetails(models.Model):
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=254)
    client_address = models.TextField()
    client_gst = models.IntegerField(max_length=15)
    biller_name = models.CharField(max_length=100)
    biller_email = models.EmailField(max_length=254)
    biller_address = models.TextField()
    biller_gst = models.IntegerField(max_length=15)
    cost_service = models.IntegerField(max_length=1000)
    tax_rate = models.IntegerField()
    bank_accounts = models.TextField()
    total_amount = models.IntegerField()

    def __str__(self):
        return self.client_name + self.biller_name

class GeneratedPdf(models.Model):
    pdf = models.FileField(upload_to ='static/pdf/')

    def __str__(self):
        return self.pdf

