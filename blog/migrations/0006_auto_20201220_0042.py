# Generated by Django 2.2.7 on 2020-12-19 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_readed_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='readed_num',
            new_name='read_num',
        ),
    ]
