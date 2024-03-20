from django.db import models
from users.models import BlogUser
from posts.models import Post


STATUS_CHOICES = (
    ("Pendente", "Pendente"),
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
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default="Aguardando Aprovação")
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
