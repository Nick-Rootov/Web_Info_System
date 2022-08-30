from django.db import models

# Create your models here.

class Dogovor(models.Model):
    number = models.PositiveIntegerField(unique=True, verbose_name='Номер договора')
    date = models.DateField(verbose_name='Дата подписания')
    #number = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Номер договора')
    zakazchik = models.CharField(max_length=60, verbose_name='Заказчик')
    n_otdela = models.ForeignKey('Otdel', on_delete=models.SET_NULL, verbose_name='Номер отдела', null=True)
    #projects = models.ManyToManyField('Project')


    def __str__(self):
        strok = str(self.number) + '-' + str(self.zakazchik)
        return strok

class Project(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название проекта')
    opis = models.CharField(max_length=100, verbose_name='Описание проекта')
    price = models.PositiveIntegerField( verbose_name='Стоимость проекта')
    dogovori = models.ManyToManyField(Dogovor, verbose_name='Договоры по проекту')



    def __str__(self):
        strok1 = str(self.id) + '-' + str(self.name)
        return strok1

class Sotrudniki (models.Model):
    last_name = models.CharField('Фамилия', max_length=40, default='')
    first_name = models.CharField('Имя', max_length=40)
    otchestvo = models.CharField('Отчество', max_length=40)
    zarplata = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Зарплата')
    cat = models.ForeignKey('Category',on_delete=models.SET_NULL,verbose_name='Категория', null=True)
    n_otdela = models.ForeignKey('Otdel', on_delete=models.SET_NULL, verbose_name='Номер отдела', null=True)
    ruk = models.BooleanField(default=False, verbose_name='Руководитель в отделе')
    #data_rojd = models.DateTimeField('Дата рождения')

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['last_name']



class Category(models.Model):
    name = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.name

class Otdel(models.Model):
    number = models.PositiveIntegerField(unique=True, verbose_name='Номер отдела')
    name = models.CharField('Наименование', max_length=30)


    def __str__(self):
        return str(self.number)


class Machine(models.Model):
    name = models.CharField('Название', max_length=30)
    opis = models.CharField('Описание', max_length=100)
    n_otdela = models.ForeignKey('Otdel', on_delete=models.SET_NULL, verbose_name='Номер отдела', null=True)

    def __str__(self):
        return self.name