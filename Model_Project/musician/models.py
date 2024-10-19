from django.db import models

# Create your models here.
# We create a models/table here named Musician
# It have attribute name, last_name, instruments
# by default it create a auto primary key named Id 
class Musician(models.Model):
    name = models.CharField(max_length=50)          # Field for the musician's first name (character limit of 50)
    last_name = models.CharField(max_length=50)     # Field for the musician's last name (character limit of 50)
    instruments = models.CharField(max_length=100)  # Field for the musician's instrument(s) (character limit of 100)

    def __str__(self):
        return self.name + " " + self.last_name + " " + self.instruments

# Create anther model named Album
# It have attribute artist(foreign key ), name, release_date, num_stars
# by default it create a auto primary key named Id
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)  # ForeignKey linking to Musician model
    name = models.CharField(max_length=100)                         # Album name (character limit of 100)
    release_date = models.DateField()                               # Album release date
    num_stars = models.IntegerField()                               # Number of stars (integer rating)


# on_delete attribute and models.CASCADE desribe it 
# models.CharField(max_length=50) #it also
# models.IntegerField()
# model.DateField() it also
# Here raise a question we didnot declared any primary key in Musician table/class but how it added as foregint key
# When we create a model class there create a auto primary key name id 
  
# Now we need to convert the class to SQL table
# first command:
# python manage.py migrate 
# second command:
# python manage.py makemigrations musician
# third command:
# python manage.py migrate 

# Describe command why it use it 

