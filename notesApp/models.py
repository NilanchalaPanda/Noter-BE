from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Note(models.Model):
    CATEGORIES_CHOICES = [
        ("BUSINESS", "Business"),
        ("PERSONAL", "Personal"),
        ("IMPORTANT", "Important"),
    ]

    title = models.CharField(max_length=100)
    body =  models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    categories = models.CharField(max_length=15, choices=CATEGORIES_CHOICES, default="PERSONAL")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.title)
            slug = slug_base
            # if Note.objects.filter(slug=slug).exists():
            #     slug = f'{slug_base}-{get_random_string(5)}'
            self.slug = slug
        super(Note, self).save(*args, **kwargs)
