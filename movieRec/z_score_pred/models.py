from django.db import models

class MovieGen(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    zscore = models.FloatField()
    gen = models.IntegerField()
    docs = models.ImageField()

    @classmethod
    def save():
        super.save()
        return "Saved signal generated"