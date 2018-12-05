from django.db import models
class announcement(models.Model):
    content = models.TextField(verbose_name="Write an announcement context")

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

