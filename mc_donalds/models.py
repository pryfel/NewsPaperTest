from django.db import models


director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Админ'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Order(models.Model):
    pass

# CREATE TABLE PRODUCTS(
# 	product_id INT AUTO_INCREMENT NOT NULL,
# 	name CHAR(255) NOT NULL,
# 	price FLOAT NOT NULL,
# 	PRIMARY KEY (product_id)
# );


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()


class ProductOrder(models.Model):
    pass
