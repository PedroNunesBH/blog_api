from django.db import models
from users.models import BlogUser
from posts.models import Post


STATUS_CHOICES = (
    ("Aguardando Aprovação", "Pendente"),
    ("Aprovado", "Aprovado"),
    ("Rejeitado", "Rejeitado")
)


class Comment(models.Model):
    author = models.ForeignKey(BlogUser,
                               on_delete=models.PROTECT,
                               related_name="author_user")  # Usuário autor do comentário
    date = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(Post,
                                  on_delete=models.PROTECT,
                                  related_name="comment_post")  # Post a qual o comentário foi feito
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, default="Aguardando Aprovação")
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

