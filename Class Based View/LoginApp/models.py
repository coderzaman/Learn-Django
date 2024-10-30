from django.db import models
from django.urls import reverse

# Create your models here.
class Poets(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address  = models.CharField(max_length=150)
    instrument = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('poet:poet_detail', kwargs={'pk':self.pk})



class Album(models.Model):
    artist = models.ForeignKey(Poets, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    RATING_CHOICES =(
        (1, "Worst"),
        (2,'Bad'),
        (3,'Okay'),
        (4,'Good'),
        (5,'Great'),
    )
    
    rating = models.IntegerField(choices=RATING_CHOICES)
    
    def __str__(self):
        return f'Name: {self.artist}, Album: {self.name}'