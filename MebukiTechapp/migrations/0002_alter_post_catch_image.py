# Generated by Django 3.2.4 on 2021-06-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MebukiTechapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='catch_image',
            field=models.CharField(max_length=200),
        ),
    ]
