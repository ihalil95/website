# Generated by Django 2.1.3 on 2018-11-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0002_remove_teaching_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaching',
            name='file',
            field=models.FileField(upload_to='teaching/', verbose_name='Upload'),
        ),
    ]