from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.CharField(max_length=100)

class blog(models.Model):
    blg = models.TextField()
    img = models.ImageField(upload_to='picture')
    dates = models.DateTimeField()
    dsc = models.TextField()
    title = models.CharField(max_length=100)
    news = models.CharField(max_length=100)
    class Meta:
        db_table="My Tables"


