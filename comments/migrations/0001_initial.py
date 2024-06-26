# Generated by Django 5.0.3 on 2024-03-20 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('users', '0002_rename_user_bloguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Aguardando Aprovação', 'Pendente'), ('Aprovado', 'Aprovado'), ('Rejeitado', 'Rejeitado')], default='Aguardando Aprovação', max_length=60)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_user', to='users.bloguser')),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment_post', to='posts.post')),
            ],
        ),
    ]
