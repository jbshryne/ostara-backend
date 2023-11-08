from django.db import models
from slugify import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.User", related_name="post", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tag, blank=True, default=None)  # Add this line

    def __str__(self):
        return self.title
