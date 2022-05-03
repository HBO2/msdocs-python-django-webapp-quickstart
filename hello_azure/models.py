from pickle import TRUE
from django.db import models

# Create your models here.

class ProjectContract(models.Model):
    ProjectContractId =  models.CharField(max_length=255)
    ProjectContractName = models.CharField(max_length=255, null=TRUE)
    ContractStartDate = models.CharField(max_length=255, null=TRUE)
    ContractEndDate =  models.CharField(max_length=255, null=TRUE)
    UpdatedAt = models.DateTimeField() 
    GrantApplicationId =  models.CharField(max_length=255, null=TRUE)

  
class Grant(models.Model):
    GrantId =  models.CharField(max_length=255)
    GrantName = models.CharField(max_length=255, null=TRUE)
    CrantStartDate = models.CharField(max_length=255, null=TRUE)
    GrantendDate =  models.CharField(max_length=255, null=TRUE)
    UpdatedAt = models.DateTimeField() 
    GContractApplicationId =  models.CharField(max_length=55, null=TRUE)

class Test(models.Model):
    TestId =  models.CharField(max_length=255)
    TestName = models.CharField(max_length=255, null=TRUE)
    TestStartDate = models.CharField(max_length=255, null=TRUE)
    TestendDate =  models.CharField(max_length=55, null=TRUE)
    UpdatedAt = models.DateTimeField() 
    TestApplicationId =  models.CharField(max_length=55, null=TRUE)

    def __str__(self): 
      return self.name 