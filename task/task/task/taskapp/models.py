from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)


    des = models.TextField()

class people(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics')
    des1 = models.TextField()


    def __str__(self):
        return self.name

    def __str__(self):
        return self.name1
