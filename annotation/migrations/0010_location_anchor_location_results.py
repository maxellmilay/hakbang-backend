# Generated by Django 5.1.1 on 2024-10-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0009_alter_coordinates_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='anchor',
            field=models.CharField(choices=[('123.9419001850121,10.327600060884297', 'Anchor A'), ('123.94220321636607,10.328668797875494', 'Anchor B'), ('123.94318663887299,10.327099440742616', 'Anchor C'), ('123.94351254051777,10.328185054214456', 'Anchor D'), ('123.94495908641485,10.32757193618587', 'Anchor E'), ('123.94445022244315,10.326536945241577', 'Anchor F')], default='123.94318663887299,10.327099440742616', max_length=50),
        ),
        migrations.AddField(
            model_name='location',
            name='results',
            field=models.JSONField(default='123.94318663887299,10.327099440742616'),
            preserve_default=False,
        ),
    ]
