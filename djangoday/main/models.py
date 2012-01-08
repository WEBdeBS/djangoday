from django.db import models

# Create your models here.

class CallForPaper(models.Model):
    titolo = models.CharField(max_length=150)
    abstract = models.TextField()
    nome =  models.CharField(max_length=150)
    cognome =  models.CharField(max_length=150)
    email = models.EmailField()
    twitter =  models.CharField(max_length=150, null=True , blank=True)
    linkedin =  models.CharField(max_length=150, null=True , blank=True)
    skype =  models.CharField(max_length=150, null=True , blank=True)
    tipo_intervento = models.CharField(max_length=20,choices=(('Overview','Overview'),('Hands On','Hands On'),('In Depth','In Depth')),verbose_name='Tipo di intervento')
    livello = models.CharField(max_length=20,choices=(('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')))