#Завдання 4

class Car:
    def __init__(self, wheels: str, speed: int, color: str):
        self.wheels = wheels
        self.speed = speed
        self.color = color

    def __str__(self):
        return f'The wheels of car: {self.wheels}, speed: {self.speed}, color: {self.color}'


car1 = Car('Michelin', 240, 'Blue')
print(car1)


class AutoShop:
    def __init__(self, name: str, year: int, price: float):
        self.name = name
        self.year = year
        self.price = price

    def car_catalog(self):
        print(f'In stock: {self.name}. Year: {self.year}, price: {self.price}')\


    def sell_car(self):
        return f'You have successfully bought {self.name}, of year {self.year}, with price {self.price}'


car2 = AutoShop('Mazda', 2003,  54000.45)
car3 = AutoShop('Ford', 2015, 120000.34)
car4 = AutoShop('Hyndai', 2011, 20000.90)

car2.car_catalog()
car3.car_catalog()
car4.car_catalog()

while True:
    select_car = int(input('Select car you would like to buy:'))
    if select_car == 1:
        print(f'{car2.sell_car()}')
    elif select_car == 2:
        print(f'{car3.sell_car()}')
    elif select_car == 3:
        print(f'{car4.sell_car()}')
    elif select_car == 4:
        print('Goodbye!')
        break
    else:
        print('Unknown action. Try again.')
        continue
