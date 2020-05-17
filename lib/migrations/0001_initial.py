# Generated by Django 2.1.3 on 2020-05-16 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('running_time', models.TimeField()),
                ('movie_discription', models.TextField()),
                ('actors_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Actor')),
                ('genre_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Genre')),
            ],
        ),
    ]
