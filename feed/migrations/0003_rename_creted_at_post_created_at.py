# Generated by Django 5.1.6 on 2025-02-20 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creted_at',
            new_name='created_at',
        ),
    ]
