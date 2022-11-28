from django.db import models

# Create your models here.

class CNABfile(models.Model):
    cnab_doc= models.FileField(unique= True)

class CNABdoc(models.Model):
    id= models.AutoField(primary_key= True)
    type= models.PositiveIntegerField()
    date= models.DateField()
    value= models.FloatField()
    cpf= models.PositiveBigIntegerField()
    card= models.CharField(max_length=50)
    hour= models.TimeField()
    owner= models.CharField(max_length=50)
    store= models.CharField(max_length=50)
    cnab_doc= models.FileField(blank= True, null= True)