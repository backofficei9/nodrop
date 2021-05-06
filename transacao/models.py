from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id_trans = models.AutoField(primary_key=True)
    nome = models.CharField("Primeiro nome", max_length=30)#models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    bin_number = models.TextField()
    trans_hora = models.DateTimeField(default=timezone.now)
    pedido_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.id_trans