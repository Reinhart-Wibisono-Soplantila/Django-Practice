from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class post(models.Model):
    # option max-length untuk panjang isi
    # option blank untuk memperboleh isi kosong (default required hilang jika blank=true)
    # option waktu auto_now_add dan fieldnya DateTimeField
    title = models.CharField(max_length=255)
    body = models.TextField()
    category =  models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(post, self).save()
    
    def __str__(self):
        return"{}. {}".format(self.id, self.title)