from django.db import models

# Create your models here.
class Music(models.Model):
    file = models.FileField(upload_to="musics/")
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False
    )
