# Generated by Django 5.0.3 on 2024-03-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_comment_author'),
        ('posts', '0012_alter_post_author'),
        ('users', '0002_rename_user_bloguser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]