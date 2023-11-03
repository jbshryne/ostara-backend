from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.User", related_name="post", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
