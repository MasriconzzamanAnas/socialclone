# Generated by Django 5.1.6 on 2025-02-23 18:58

import feed.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_post_catagory_alter_post_img_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=feed.models.postfile),
        ),
    ]
