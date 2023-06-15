from django.db import models 

#Inherits from models.Model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()


#In database newly entered data is shown as 'OBJECT'
#To FIX, change string representation of object, by overriding method 
    def __str__(self): #self as arg to refer to attributes on obj instance
        return f'{self.title} from {self.year}' #info to get as string representation




  