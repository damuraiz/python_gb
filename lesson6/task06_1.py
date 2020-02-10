# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import datetime, time
import itertools


class TrafficLight:
    """red - 7 sec, yellow - 2 sec, green - 6 sec"""
    # proper_mode = {"time": {"red": 7, "yellow": 2, "green": 6},
    #                "next": {"red": "yellow", "yellow": "green", "green": "red"}}

    proper_mode = [("red", 7), ("yellow", 2), ("green", 6)]

    def __init__(self, order=["red", "yellow", "green"], durations=[7, 2, 6]):
        self.__mode = list(zip(order, durations))

    def get_color(self):
        return self.__color

    def __self_check(self):
        if TrafficLight.proper_mode != self.__mode:
            raise Exception({"mode": self.__mode})

    def running(self):
        self.__self_check()
        for mode in itertools.cycle(self.__mode):
            self.__color=mode[0]
            print(f'{datetime.datetime.now():%H:%M:%S}: светофор включил {self.get_color()} цвет')
            time.sleep(mode[1])



traffic_light = TrafficLight(durations=[7, 2, 6])
#остановку светофора пилить не стал. тут вроде как этого не просили. Так что бесконечный светофор=)
traffic_light.running()
