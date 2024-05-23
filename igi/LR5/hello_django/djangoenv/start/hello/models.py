from django.db import models


#Тип услуг
class ServiceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#Услуга
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    type = models.ForeignKey(ServiceType, related_name="services", on_delete=models.CASCADE)

    def __str__(self):
        return self.naming



#ex: audi, bmw
class CarModel(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

#Тип авто
class CarType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Клиент
class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField() #min = 18
    phone_number = models.CharField(max_length=19) # +375 (44) xxx-xx-xx
    result_price = models.PositiveIntegerField() #for promocode
    car_model = models.ForeignKey(CarModel, related_name="clients", on_delete=models.DO_NOTHING)
    car_type = models.ForeignKey(CarType, related_name="clients", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name()


#Специализация мастеров
class Specialization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Мастер
class Master(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=19)
    specialization = models.ForeignKey(Specialization, related_name="masters", on_delete=models.CASCADE,  default=None)
    order_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name



#Вид запчастей
class PartType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Запчасть
class Part(models.Model):
    name = models.CharField(max_length=20)
    car_model = models.ForeignKey(CarModel, related_name="parts", on_delete=models.CASCADE, default=None)
    price = models.PositiveIntegerField()
    type = models.ForeignKey(PartType, related_name="parts", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


#Промокод
class Promocode(models.Model):
    name = models.CharField(max_length=15)
    discount = models.PositiveSmallIntegerField()

#Заказ
class Order(models.Model):
    master = models.ForeignKey(Master, related_name="orders", on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(Client, related_name="orders", on_delete=models.CASCADE, default=None)
    whole_price = models.PositiveIntegerField()
    ordering_time = models.DateTimeField()
    service = models.ForeignKey(Service, related_name="orders", on_delete=models.DO_NOTHING)

    def CountPrice(self, prom = None, parts = None):
        price = self.service.price
        if parts:
            for p in parts:
                price += p.price
        if prom:
            price *= (100-prom.discount)
        return price



