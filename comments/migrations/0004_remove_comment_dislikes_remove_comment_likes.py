# Generated by Django 5.0.3 on 2024-03-22 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
