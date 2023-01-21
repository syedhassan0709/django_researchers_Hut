from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Year(models.Model):
    year =  models.IntegerField(validators=[MinValueValidator(2005),MaxValueValidator(2023)],unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        y = str(self.year)
        return y
class Field(models.Model):
    level = models.CharField(max_length=15)

    def __str__(self):
        return self.level
class Publication(models.Model):
    year = models.ForeignKey(Year,on_delete = models.CASCADE)
    level = models.ForeignKey(Field,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.TextField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'publications'

    def __str__(self) :
        return self.text[:50]
            
            
       
        


    