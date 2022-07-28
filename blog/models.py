from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profiles_api.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() # Variable que guarda el manejador de objetos, punto crucial para hacer las consultas.
    postobjects = PostObjects() 

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
