from django.db import models
    
# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def _str_(self):  # new
        return self.text[:50]
