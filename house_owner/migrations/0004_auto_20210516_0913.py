# Generated by Django 2.2.14 on 2021-05-16 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_owner', '0003_houses_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='image1',
            field=models.ImageField(upload_to='static/images/houses/'),
        ),
        migrations.AlterField(
            model_name='houses',
            name='image2',
            field=models.ImageField(upload_to='static/images/houses/'),
        ),
        migrations.AlterField(
            model_name='houses',
            name='image3',
            field=models.ImageField(upload_to='static/images/houses/'),
        ),
    ]