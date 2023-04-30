# Generated by Django 4.2 on 2023-04-29 05:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_image', models.ImageField(upload_to='movies_posters/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_started', models.DateTimeField()),
                ('time_ended', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.show')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(300)])),
                ('show_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.show')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
