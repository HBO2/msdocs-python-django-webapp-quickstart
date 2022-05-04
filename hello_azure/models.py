from pickle import TRUE
from django.db import models

# Create your models here.

class ProjectContract(models.Model):
    ProjectContractId =  models.CharField(max_length=255)
    ProjectContractName = models.CharField(max_length=255, null=True)
    ContractStartDate = models.CharField(max_length=255, null=True)
    ContractEndDate =  models.CharField(max_length=255, null=True)
    UpdatedAt = models.DateTimeField() 
    GrantApplicationId =  models.CharField(max_length=255, null=True)
    def __str__(self): 
      return self.name 
  
class Grant(models.Model):
    GrantId =  models.CharField(max_length=255)
    GrantName = models.CharField(max_length=255, null=True)
    CrantStartDate = models.CharField(max_length=255, null=True)
    GrantendDate =  models.CharField(max_length=255, null=True)
    UpdatedAt = models.DateTimeField() 
    GContractApplicationId =  models.CharField(max_length=55, null=True)
    def __str__(self): 
      return self.name 
class Test(models.Model):
    TestId =  models.CharField(max_length=255)
    TestName = models.CharField(max_length=255, null=True)
    TestStartDate = models.CharField(max_length=255, null=True)
    TestendDate =  models.CharField(max_length=55, null=True)
    TestApplicationId =  models.CharField(max_length=55, null=True)
    
    def __str__(self): 
      return self.name 