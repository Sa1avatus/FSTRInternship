# Generated by Django 4.1.7 on 2023-02-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patronymic_name',
            field=models.CharField(default=1, max_length=255, verbose_name='last name'),
            preserve_default=False,
        ),
    ]
