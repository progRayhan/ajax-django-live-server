from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, verbose_name="Name")
    message = models.CharField(max_length=200, blank=False, verbose_name="Message")
    email = models.EmailField(max_length=50, blank=False, verbose_name="Email")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name
    
    
    