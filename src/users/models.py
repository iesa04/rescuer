from django.db import models

class UserType(models.Model):
	user_type_code = models.CharField(max_length=2)
	user_type_name = models.CharField(max_length=50)

class Users(models.Model):
    user_id		        = models.IntegerField() 
    username 			= models.CharField(max_length = 50)
    password 			= models.CharField(max_length = 30)
    name 				= models.CharField(max_length = 100)
    user_type_code 		= models.CharField(max_length = 2)

class AdminDetail(models.Model):
    user_id             = models.IntegerField() 
    username            = models.CharField(default = "test",max_length = 50)
    password            = models.CharField(default = "test",max_length = 30)
    name                = models.CharField(default = "test",max_length = 100)
    user_type_code      = models.CharField(default = "AD",max_length = 2)
    admin_phone_number 	= models.CharField(max_length = 10)

class CustomerDetail(models.Model):
    user_id             = models.IntegerField() 
    username            = models.CharField(default = "test",max_length = 50)
    password            = models.CharField(default = "test",max_length = 30)
    name                = models.CharField(default = "test",max_length = 100)
    user_type_code      = models.CharField(default = "CT",max_length = 2)
    FDID 				= models.CharField(max_length = 5)

class SupplierDetail(models.Model):
    user_id             = models.IntegerField() 
    username            = models.CharField(default = "test",max_length = 50)
    password            = models.CharField(default = "test",max_length = 30)
    name                = models.CharField(default = "test",max_length = 100)
    user_type_code      = models.CharField(default = "SU",max_length = 2)
    supplier_state 		= models.CharField(max_length = 50)

