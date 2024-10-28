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