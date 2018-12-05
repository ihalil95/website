from django.db import models

class assists(models.Model):
    CHOICES = (
    ('Research Assistant', ('Research Assistant')),
    ('PhD Student', ('PhD Student')),
    )
    photo = models.CharField(verbose_name="Photo url",max_length=1000)
    name = models.CharField(max_length=250,verbose_name="Full name")
    duty = models.CharField(verbose_name="Position",choices=CHOICES,max_length=1000)
    detail = models.TextField(verbose_name="About")
    class Meta:
        verbose_name = 'Assistant'
        verbose_name_plural = 'Assistants'
