from django.db import models

# Create your models here.
class Poetry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Album(models.Model):
    artist = models.ForeignKey(Poetry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    RATING_CHOICES = (
        (1,'Worst'),
        (2,'Bad'),
        (3,'Okay'),
        (4,'Good'),
        (5,'Great'),
    )
    
    num_stars = models.IntegerField(choices=RATING_CHOICES)



    def __str__(self):
        return f'Artist: {self.artist}, Album: {self.name}, Release Date: {self.release_date}, Rating: {self.num_stars}'