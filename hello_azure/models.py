from pickle import TRUE
from django.db import models

# Create your models here.

class ProjectContract(models.Model):
    ProjectContractId =  models.CharField(max_length=255)
    ProjectContractName = models.CharField(max_length=255, null=TRUE)
    ContractStartDate = models.DateTimeField()
    ContractEndDate =  models.CharField(max_length=255, null=TRUE)
    UpdatedAt = models.DateTimeField() 
    GrantApplicationId =  models.CharField(max_length=255, null=TRUE)


    def __str__(self): 
      return self.name 