# Ex02 Django ORM Web Application
## Date: 28.10.24


## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).
## ENTITY RELATIONSHIP DIAGRAM
![web ex 2 mind map](https://github.com/user-attachments/assets/3e1f71c9-6082-4e92-aab7-f8a1b5ab3bc0)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import Bank,BankAdmin
admin.site.register(Bank,BankAdmin)

models.py
from django.db import models
from django.contrib import admin
class Bank (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    dateofbirth=models.IntegerField()              
    amount=models.IntegerField()
    refno=models.IntegerField()

class BankAdmin(admin.ModelAdmin):
    list_display=('name','refno','age','dateofbirth','amount')

```
## OUTPUT

![alt text](<web bank exp 2.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
