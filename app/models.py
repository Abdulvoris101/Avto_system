from django.db import models

# Create your models here.


class Avtomobil(models.Model):
    nomi = models.CharField(max_length=200)
    yil = models.IntegerField()
    rasm = models.ImageField(upload_to='avto_rasmlar',null=True, blank=True)
    manzil =  models.CharField(max_length=200)
    probeg = models.IntegerField()
    kuzov = models.CharField(max_length=200)
    dvigatel = models.CharField(max_length=200)
    rang = models.CharField(max_length=200)
    narx = models.IntegerField()
    tel_nomer = models.IntegerField()
    xarakteristika = models.CharField(max_length=200)


    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'
    