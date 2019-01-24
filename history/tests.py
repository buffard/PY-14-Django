from django.test import TestCase

# Create your tests here.
def test_list_artists(self):
  new_artist = Artists.objects.create(
    name="Suzy Saxophone"
    birth_date="12/25/58"
  )