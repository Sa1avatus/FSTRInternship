# Generated by Django 4.1.7 on 2023-02-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0004_alter_cords_latitude_alter_cords_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='added',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default=('new', 'new'), max_length=100),
        ),
    ]