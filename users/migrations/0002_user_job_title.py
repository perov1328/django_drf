# Generated by Django 4.2.7 on 2023-12-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job_title',
            field=models.CharField(choices=[('User', 'User'), ('Moderator', 'Moderator')], default='User', max_length=15),
        ),
    ]