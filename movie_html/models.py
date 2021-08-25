from django.db import models


class videos(models.Model):
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(blank=False, max_length=500)
    video = models.FileField(upload_to="videos/", default="none")

    class Meta:
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.file_name