class Car:
    pass

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новый авто: {self.name} (цвет {self.color}) авто полицейский - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}.'


class TownCar(Car):
    pass

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. Превышение скорости' \
            if self.speed > 60 else f'{self.name}: Скорость авто {self.speed}'

class WorkCar(Car):
    pass

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. Превышение скорости' \
            if self.speed > 40 else f'{self.name}: Скорость авто {self.speed}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar("Бобик", 'белый', 90)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()

police_car = WorkCar("Таблетка", 'болотная', 40)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()

police_car = SportCar("Ламба", 'жёлтая', 190)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()

