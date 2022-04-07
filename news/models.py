from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from profiles.models import UserProfile

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    tag_name = models.CharField(max_length=70)
    friendly_name = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.tag_name

    def get_friendly_name(self):
        return self.friendly_name


class NewsPost(models.Model):
    """
    Where the news post is created
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    post_title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        UserProfile, related_name='news_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.post_title

    def number_of_likes(self):
        return self.likes.count()
