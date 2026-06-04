from django.db import models

# Create your models here.
class News(models.Model):
    headline=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateField()
    # url=models.URLField(blank=True)