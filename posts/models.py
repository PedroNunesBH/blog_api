from django.db import models
from users.models import BlogUser
from django.contrib.auth.models import User

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
    status = models.CharField(max_length=80, choices=STATUS_CHOICES, default="Pendente")

    def __str__(self):
        return self.title


class PostLikeAndDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_post_like_dislike")
    post = models.ForeignKey(Post,
                             on_delete=models.PROTECT,
                             related_name="post_like_dislike")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
