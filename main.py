import string


class Car:
    def __init__(self, brand, color, engine_capacity):
        self.__brand = brand
        self.__color = color
        self.__engine_capacity = engine_capacity

    def move_forward(self):
        print("The car is moving forward")

    def move_backward(self):
        print("The car is moving backward")


class CarUpd(Car):
    def move_left(self):
        print("The car is going to the left")

    def move_right(self):
        print("The car is going to the right")


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.__clean_text = ""
        self.__punktuation = string.punctuation

    def get_clean_text(self):
        for i in range(len(self.text)):
            if not self.__is_punctiantian(self.text[i]):
                self.__clean_text += self.text[i]
        print(self.__clean_text)

    def __is_punctiantian(self, symb):
        if symb in self.__punktuation:
            return True
        else:
            return False


car = Car("Volvo", "Orange", 2.0)
car.move_forward()
car.move_backward()

car_upd = CarUpd("Volvo", "Orange", 2.0)
car_upd.move_forward()
car_upd.move_backward()
car_upd.move_right()
car_upd.move_left()

proc = TextProcessor("hghgh./ghger''4326bgfdn")
proc.get_clean_text()
