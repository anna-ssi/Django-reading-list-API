# Generated by Django 2.1.5 on 2019-06-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190625_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
