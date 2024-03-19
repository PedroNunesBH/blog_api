from django.db import models


class BlogUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    register_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
