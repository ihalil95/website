from django.db import models
from django.http import HttpResponse
class teaching(models.Model):
    TYPE_CHOICES = (
        ('Concrete Mix Design', ('Concrete Mix Design')),
        ('Betonarme', ('Betonarme')),
        ('Structural Mechanics',('Structural Mechanics')),
        ('Betonarmede kırılma mekaniği',('Betonarmede kırılma mekaniği'))
    )
    lecture = models.CharField(max_length=1000, verbose_name="Name of course", choices=TYPE_CHOICES,
                               default='Betonarme')
    title = models.CharField(max_length=1000, verbose_name="Title")
    file = models.FileField(verbose_name="Upload",upload_to='teaching/')
    class Meta:
        verbose_name = 'Teaching'
        verbose_name_plural = 'Teachings'
