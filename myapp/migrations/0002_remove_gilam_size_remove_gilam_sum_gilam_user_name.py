# Generated by Django 4.2.2 on 2023-07-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gilam',
            name='size',
        ),
        migrations.RemoveField(
            model_name='gilam',
            name='sum',
        ),
        migrations.AddField(
            model_name='gilam',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]