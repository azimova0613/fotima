from django.db import models

# Create your models here.
class story(models.Model):
    nomi=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    text=models.TextField()

class story2(models.Model):   
    nomi=models.CharField(max_length=100)
    narx=models.FloatField()
    title=models.CharField(max_length=200)
    nomi2=models.CharField(max_length=100)

class story3(models.Model):
    nomi=models.CharField(max_length=100)
    nomi=models.CharField(max_length=50)
    title=models.CharField(max_length=100)

class story4(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()

class story5(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()


class story6(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()

class story7(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()


class story8(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()


class story9(models.Model):
    nomi=models.CharField(max_length=100)

class story14(models.Model):
    nomi=models.CharField(max_length=100)
    narx=models.FloatField()
    image=models.ImageField(upload_to='media/')
    xarid=models.CharField(max_length=100)

class story15(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=50)
    title=models.CharField(max_length=100)

class story16(models.Model):
    nomi=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/')
    nomi2=models.CharField(max_length=100)
    title=models.CharField(max_length=100)

class story17(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=50)
    title=models.CharField(max_length=100)

class story18(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    
class story19(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()

class story20(models.Model):
    nomi=models.CharField(max_length=100)
    adres=models.CharField(max_length=100)
    adres2=models.CharField(max_length=100)
    tel2=models.CharField(max_length=100)
    tel=models.FloatField()
    email=models.CharField(max_length=100)

class story21(models.Model):
    nomi=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/')

class story22(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=50)
    emailid=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)
        
class shop1(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=50)
    title=models.CharField(max_length=100)

class kantak(models.Model):
    nomi=models.CharField(max_length=100)
    text=models.TextField()

class kantakt2(models.Model):
    Username=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone=models.FloatField()
    massage=models.CharField(max_length=100)


class march(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)
    text=models.TextField()

class camment(models.Model):
    nomi=models.CharField(max_length=100)
    sana=models.CharField(max_length=100)
    text=models.TextField()
    nomi2=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/') 

class izoh(models.Model):
    # nomi=models.CharField(max_length=100)
    ism=models.CharField(max_length=100)
    mavzu=models.CharField(max_length=100)
    text=models.TextField()
    email=models.CharField(max_length=100)

class post(models.Model):
   
    sana=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField(upload_to='media/') 

class post2(models.Model):
    nomi=models.CharField(max_length=100)  
    nomi=models.CharField(max_length=100)
    narx=models.FloatField()
    title=models.CharField(max_length=200)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)
    nomi=models.CharField(max_length=100)

class xarid(models.Model):
    narx=models.FloatField()
    title=models.CharField(max_length=100)
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)
    nomi4=models.CharField(max_length=100)
   

class xarid2(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    text=models.TextField()

class xarid3(models.Model):
    title=models.CharField(max_length=100)

class loyiha(models.Model):
    nomi=models.CharField(max_length=100)
    title=models.CharField(max_length=100)

class page(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)

class jamoa(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)

class jamoa2(models.Model):
    nomi=models.CharField(max_length=100)
    nomi2=models.CharField(max_length=100)
    nomi3=models.CharField(max_length=100)

class dehqon(models.Model):
    text=models.TextField()
    text2=models.TextField()
    nomi=models.CharField(max_length=100)
    

    
    




