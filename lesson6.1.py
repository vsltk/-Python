from time import sleep


class TrafficLight:
    __color = "Black"


    def running(self):
        while True:
            print('Red color!')
            sleep(7)
            print('Yellow color!')
            sleep(2)
            print('Green color!')
            sleep(9)
            print('Yellow color!')
            sleep(2)


tl = TrafficLight()
tl.running()
