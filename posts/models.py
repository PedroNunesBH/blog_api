from django.db import models
from users.models import BlogUser

STATUS_CHOICES = (
    ("Pendente", "Pendente"),
    ("Aprovado", "Aprovado"),
    ("Rejeitado", "Rejeitado")
)


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author = models.ForeignKey(BlogUser,
                               on_delete=models.PROTECT,
                               related_name="post_author_user")  # ID do usuário autor do post
    content = models.CharField(max_length=500)
    status = models.CharField(max_length=80, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
