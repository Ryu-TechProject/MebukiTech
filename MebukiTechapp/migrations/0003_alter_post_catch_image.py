# Generated by Django 3.2.4 on 2021-06-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MebukiTechapp', '0002_alter_post_catch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='catch_image',
            field=models.TextField(),
        ),
    ]
