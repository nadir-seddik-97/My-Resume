# Generated by Django 3.2.8 on 2021-10-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
