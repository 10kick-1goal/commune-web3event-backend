from django.db import models


class EventUrl(models.Model):
    source_url = models.CharField(max_length=200)
    site_type = models.CharField(max_length=5, default="0")

    def __str__(self):
        return self.source_url


class City(models.Model):
    city_href = models.CharField(max_length=20)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Web3event(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='images/') 
    organizers = models.CharField()
    address = models.CharField()
    time = models.CharField()
    description = models.CharField()
    presenter = models.CharField()
    tags = models.CharField()

    def __str__(self):
        return self.title
        
    
