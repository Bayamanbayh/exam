# Generated by Django 5.2.1 on 2025-06-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skill',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill',
            field=models.ManyToManyField(blank=True, null=True, to='fl.skill'),
        ),
    ]
