# Generated by Django 4.0.3 on 2022-07-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipleapp', '0004_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='allimgess'),
        ),
    ]
