# Generated by Django 2.1.5 on 2019-06-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('rating_count', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]