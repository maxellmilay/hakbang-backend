# Generated by Django 5.1.1 on 2024-10-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0008_location_accessibility_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='latitude',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='longitude',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='coordinates',
            unique_together={('latitude', 'longitude')},
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('start_coordinates', 'end_coordinates')},
        ),
    ]
