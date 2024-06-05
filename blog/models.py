from django.db import models

# Create your models here.

class post(models.Model):
    # option max-length untuk panjang isi
    # option blank untuk memperboleh isi kosong (default required hilang jika blank=true)
    # option waktu auto_now_add dan fieldnya DateTimeField
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default='namaweb.com')
    
    def __str__(self):
        return"{}".format(self.title)