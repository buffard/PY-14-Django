from django.db import models

# Build a model representing your Artist table.
class Artists(models.Model):
  name = models.CharField(max_length=35)
  established = models.CharField(max_length=4)

  def __str__(self):
    ''' returns a string representation of the model '''
    return self.name

class Songs(models.Model):
  name = models.CharField(max_length=35)
  pub_date = models.CharField(max_length=20)
  artistid = models.ForeignKey(Artists, on_delete=models.CASCADE)
  def __str__(self):
    ''' returns a string representation of the model '''
    return self.name
