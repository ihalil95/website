from django.db import models

class researches(models.Model):
    title = models.CharField(verbose_name="Title",max_length=1000)
    keywords = models.CharField(verbose_name="Keywords",max_length=1000)
    keypublication = models.CharField(verbose_name="Key Publication",max_length=1000)
    abstract = models.TextField(verbose_name="Abstract")
    date = models.DateField(verbose_name="Publishing date")

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'
