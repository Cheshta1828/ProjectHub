# Generated by Django 4.2.5 on 2023-09-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectentry',
            name='image1',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='image2',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='image3',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
    ]