from django.db import models

class ID(models.Model):
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=72)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='clients')
    doc_id = models.OneToOneField(ID, null=True, on_delete=models.CASCADE)

    def get_fullname(self):
        return self.name +" " + self.last_name

    def __str__(self):
        return self.get_fullname()

class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    taxes = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.description

class Sale(models.Model):
    sale_number = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    products = models.ManyToManyField(Product, null=True, blank=True)

    def __str__(self):
        return self.sale_number