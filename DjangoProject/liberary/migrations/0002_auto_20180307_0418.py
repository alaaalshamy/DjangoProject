# Generated by Django 2.0.3 on 2018-03-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='date_birth',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='witer_name',
        ),
        migrations.AddField(
            model_name='writer',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Died'),
        ),
        migrations.AddField(
            model_name='writer',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
