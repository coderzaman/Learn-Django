from django.db import models

class Musician(models.Model):
    name = models.CharField(max_length=50)          # First name of the musician
    last_name = models.CharField(max_length=50)     # Last name of the musician
    instruments = models.CharField(max_length=100)  # Instrument(s) the musician plays

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.instruments}"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)  # Link to Musician
    name = models.CharField(max_length=100)                         # Album name
    release_date = models.DateField()                               # Album release date

    # Rating choices (similar to HTML <select> dropdown options)
    RATING_CHOICES = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    num_stars = models.IntegerField(choices=RATING_CHOICES)         # Rating field with choices

    def __str__(self):
        return f"{self.name} ({self.release_date}) - Rating: {self.num_stars} Stars by {self.artist}"

    

