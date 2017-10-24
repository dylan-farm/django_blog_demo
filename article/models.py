from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Acticle(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:9008%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
