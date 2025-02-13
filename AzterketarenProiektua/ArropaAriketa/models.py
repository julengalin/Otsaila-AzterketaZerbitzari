from django.db import models

# Create your models here.
class Jantzia(models.Model):
    id = models.AutoField(primary_key=True)
    deskripzioa = models.CharField(max_length=75)
    kolorea = models.CharField(max_length=75)
    kopurua = models.IntegerField()

    def __str__(self):
        return f"{self.deskripzioa} {self.kolorea} ({str(self.kopurua)})"
    
class Diseinatzailea(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=75)
    helbidea = models.CharField(max_length=75)
    emaila = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.izena} {self.abizena} {self.helbidea} {self.emaila})"

class Bilduma(models.Model):
    jantzia = models.ForeignKey(Jantzia, on_delete=models.CASCADE)
    diseinatzailea = models.ForeignKey(Diseinatzailea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.diseinatzailea.izena} {self.jantzia.id}"