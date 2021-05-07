class Stationery:
    def __init__(self, title='инструмент'):
        self.title = title

    def draw(self):
        print(f'Давай порисуем! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Используй для рисунка {self.title} ручку!')


class Pencil(Stationery):
    def draw(self):
        print(f'Используй для рисунка {self.title} карандаш!')

class Handle(Stationery):
    def draw(self):
        print(f'Используй для рисунка {self.title} маркер!')


st = Stationery()
st.draw()
pen = Pen("Конус")
pen.draw()
pencil = Pencil("ErichKrause")
pencil.draw()
marker = Handle("TouchTwin")
marker.draw()


