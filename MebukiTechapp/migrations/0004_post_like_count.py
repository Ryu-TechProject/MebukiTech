# Generated by Django 3.2.4 on 2021-06-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MebukiTechapp', '0003_alter_post_catch_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
