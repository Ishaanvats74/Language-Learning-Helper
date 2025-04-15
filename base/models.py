from django.db import models

# Create your models here.


class About_US(models.Model) :
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True ,blank= True)
    # participants = 
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
    

class Message(models.Model):
    # host = 
    # topic =
    about_us = models.ForeignKey(About_US, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name