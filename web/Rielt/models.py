from django.db import models

# Create your models here. rent


class Sale(models.Model):
    status_choice=[(1,"Продано"),(0,"Не продано")]
    uid=models.IntegerField(verbose_name="Айди квартиры",unique=True)
    district=models.CharField(verbose_name="Район",max_length=100)
    orient=models.CharField(max_length=200,verbose_name="Ориентир")
    room_number=models.IntegerField(verbose_name="Кол-во комнат")
    floor=models.CharField(max_length=6,verbose_name="Этаж/Высота")
    street=models.CharField(max_length=50,verbose_name="Улица")
    square=models.FloatField(verbose_name="Площадь")
    mater=models.CharField(max_length=50,verbose_name="Материал")
    condition_of_repair=models.CharField(max_length=15,verbose_name="Состояние ремонта")
    price=models.CharField(max_length=50,verbose_name="Цена")
    telephon_number=models.CharField(max_length=15,verbose_name="Телефон")
    name=models.CharField(max_length=50,verbose_name="Ф.И.О")
    longitude=models.CharField(max_length=20,verbose_name="Долгота") #долгота
    latitude=models.CharField(max_length=20,verbose_name="Широта") #широта
    photo=models.CharField(max_length=100,verbose_name="Ссылка на фото")
    status=models.IntegerField(verbose_name="Статус",default=0,choices=status_choice)
    dop_id=models.IntegerField(verbose_name="ID риэлтора")
    class Meta:
        verbose_name="Продажа"
        verbose_name_plural="Продажа"

class Rent(models.Model):
    status_choice=[(1,"Занято"),(0,"Свободно")]
    uid=models.IntegerField(verbose_name="Айди квартиры",unique=True)
    district=models.CharField(verbose_name="Район",max_length=100)
    orient=models.CharField(max_length=50,verbose_name="Ориентир")
    room_number=models.IntegerField(verbose_name="Кол-во комнат")
    floor=models.CharField(max_length=6,verbose_name="Этаж/Высота")
    street=models.CharField(max_length=50,verbose_name="Улица")
    square=models.FloatField(verbose_name="Площадь")
    condition_of_repair=models.CharField(max_length=15,verbose_name="Состояние ремонта")
    furniture=models.CharField(max_length=100,verbose_name="Обстановка")
    price=models.CharField(max_length=50,verbose_name="Цена в месяц")
    telephon_number=models.CharField(max_length=15,verbose_name="Телефон")
    name=models.CharField(max_length=50,verbose_name="Ф.И.О")
    longitude=models.CharField(max_length=20,verbose_name="Долгота") #долгота
    latitude=models.CharField(max_length=20,verbose_name="Широта") #широта
    photo=models.CharField(max_length=100,verbose_name="Ссылка на фото",default="-----")
    status=models.IntegerField(verbose_name="Статус",default=0,choices=status_choice)
    class Meta:
        verbose_name="Аренда"
        verbose_name_plural="Аренда"

class New_builds(models.Model):
    uid=models.IntegerField(verbose_name="Айди квартиры",unique=True)
    district=models.CharField(verbose_name="Район",max_length=100)
    street=models.CharField(max_length=50,verbose_name="Улица")
    builder=models.CharField(max_length=50,verbose_name="Застройщик")
    reput=models.CharField(max_length=6,verbose_name="Репутация застройщика")
    compl=models.CharField(max_length=50,verbose_name="Жилой комплекс")
    date=models.IntegerField(verbose_name="Год постройки")
    price=models.CharField(max_length=50,verbose_name="Цена за 1 кв.м от")
    ostat=models.IntegerField(verbose_name="Площадь")
    parking=models.IntegerField(verbose_name="Парковочных мест")
    security=models.CharField(max_length=100,verbose_name="Охраняемая территория")
    child=models.CharField(max_length=5,verbose_name="Детский двор")
    struct=models.CharField(max_length=100,verbose_name="Инфраструктура")
    uprava=models.CharField(max_length=50,verbose_name="Управляющая компания")
    longitude=models.CharField(max_length=20,verbose_name="Долгота") #долгота
    latitude=models.CharField(max_length=20,verbose_name="Широта") #широта    
    photo=models.CharField(max_length=100,verbose_name="Ссылка на фото",default="-----")
    file_id=models.CharField(max_length=50,verbose_name="Ссылка на файл")
    phone=models.CharField(max_length=15,verbose_name="Телефон")
    dop_id=models.IntegerField(verbose_name="ID застройщика")
    class Meta:
        verbose_name="Новостройка"
        verbose_name_plural="Новостройки"

class Users(models.Model):
    choices=[(0,"Нет"),(1,"Да")]
    name=models.CharField(max_length=50,verbose_name="Имя")
    phone=models.CharField(max_length=15,verbose_name="Номер телефона")
    status=models.IntegerField(verbose_name="Зарегистрирован",choices=choices)
    user_id=models.IntegerField(verbose_name="Айди")
    filt=models.CharField(verbose_name="Фильтр",max_length=100)
    class Meta:
        verbose_name="Подписчики"
        verbose_name_plural="Подписчики"

class Admins(models.Model):
    name=models.CharField(max_length=50,verbose_name="Имя")
    district=models.CharField(max_length=100,verbose_name="Район")
    admin_id=models.IntegerField(verbose_name="Айди")
    class Meta:
        verbose_name="Администраторы"
        verbose_name_plural="Администраторы"