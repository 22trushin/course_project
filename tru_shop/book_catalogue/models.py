from django.conf import settings
from django.db import models
from django.db.models import Manager, DO_NOTHING
from django.utils import timezone
from django.db.models.signals import post_save, m2m_changed
from django.utils.text import get_valid_filename

# Create your models here.

class BooksCatalogue(models.Model):
    genre = models.CharField(max_length=30)
    subgenre = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    series = models.CharField(max_length=20)
    publishing_house = models.CharField(max_length=30)
    year_of_publishing = models.IntegerField()
    count_of_pages = models.IntegerField()
    isbn = models.IntegerField()
    edition = models.IntegerField()
    format = models.CharField(max_length=20)
    cover_type = models.CharField(max_length=20)
    annotation = models.CharField(max_length=5000)
    cover_img = models.ImageField()
    price = models.FloatField()
