from django.db import models
class homework(models.Model):
    TYPE_CHOICES = (
        ('Concrete Mix Design', ('Concrete Mix Design')),
        ('Betonarme', ('Betonarme')),
        ('Structural Mechanics','Structural Mechanics'),
        ('Betonarmede kırılma mekaniği','Betonarmede kırılma mekaniği')
    )
    deadline = models.DateField(verbose_name="Deadline")
    givendate = models.DateField(verbose_name="The date when the homework was given",default="")
    homeworkname = models.CharField(max_length=1000,verbose_name="Homework title")
    lecture = models.CharField(max_length=1000,verbose_name="Name of this course",choices=TYPE_CHOICES,default='Betonarme')
    desc = models.TextField(verbose_name="explanation for this homework",default="")
    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homeworks'
class posthomework(models.Model):
    TYPE_CHOICES = (
        ('Concrete Mix Design', ('Concrete Mix Design')),
        ('Betonarme', ('Betonarme')),
        ('Structural Mechanics', 'Structural Mechanics'),
        ('Betonarmede kırılma mekaniği', 'Betonarmede kırılma mekaniği')
    )
    studentnumber = models.CharField(verbose_name="Student number",max_length=1000)
    date = models.DateField(verbose_name="Recieved date",auto_now_add=True)
    files = models.FileField(verbose_name="Upload your homework",upload_to='homeworks')
    grade = models.IntegerField(default="0",blank=True)
    coursename = models.CharField(verbose_name="Course name",max_length=1000,choices=TYPE_CHOICES,default='Betonarme')
    workname = models.CharField(verbose_name="Homework name",max_length=1000)
    class Meta:
        verbose_name = 'Recieved homework'
        verbose_name_plural = 'Recieved homeworks'