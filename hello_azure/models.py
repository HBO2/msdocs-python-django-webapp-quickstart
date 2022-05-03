from pickle import TRUE
from django.db import models

# Create your models here.

class Contact(models.Model): 
   name = models.CharField(max_length=50) 
   city = models.CharField(max_length=50) 
   state = models.CharField(max_length=2) 
   create_date = models.DateTimeField() 
   phone_number = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 

class ProjectContract(models.Model):
    ProjectContractId =  models.CharField(max_length=255)
    ProjectContractName = models.CharField(max_length=255, null=TRUE)
    ContractStartDate = models.CharField(max_length=255, null=TRUE)
    ContractEndDate =  models.CharField(max_length=255, null=TRUE)
    UpdatedAt = models.DateTimeField() 
    GrantApplicationId =  models.CharField(max_length=255, null=TRUE)

def __str__(self): 
      return self.name 