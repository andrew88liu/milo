# Generated by Django 2.0.1 on 2018-02-16 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0003_auto_20180216_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('workout_date', models.DateTimeField(verbose_name='workout date')),
                ('attendees', models.ManyToManyField(related_name='workouts_workoutsession_related', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='workoutsessions',
            name='attendees',
        ),
        migrations.RemoveField(
            model_name='workoutsessions',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='WorkoutSessions',
        ),
    ]
