import csv
from os.path import splitext


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if brand == "":
            raise RuntimeError("empty brand")
        elif photo_file_name == "":
            raise RuntimeError("empty photo_file_name")
        elif carrying == "":
            raise RuntimeError("empty carrying")
        self.car_type = str()
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        if self.get_photo_file_ext() not in [".jpg", ".jpeg", ".png", ".gif"]:
            raise RuntimeError("invalid photo_file_name")

    def __str__(self):
        return self.car_type

    def __repr__(self):
        return self.car_type

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        if passenger_seats_count == "":
            raise RuntimeError("empty passenger_seats_count")
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        # if body_whl == "":
        #     raise RuntimeError("empty body_whl")
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
        self.body_whl(body_whl)

    def body_whl(self, whl):
        try:
            body_length, body_width, body_height = whl.split(
                'x')   # mind the order
            self.body_width = float(body_width)
            self.body_height = float(body_height)
            self.body_length = float(body_length)
        except BaseException:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        if extra == "":
            raise RuntimeError("empty extra")
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def parse_row(row):
    try:
        car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
        # print(car_type)
        # print(brand)
        # print(passenger_seats_count)
        # print(photo_file_name)
        # print(body_whl)
        # print(carrying)
        # print(extra)
        if car_type == "car":
            return Car(brand, photo_file_name, carrying, passenger_seats_count)
        elif car_type == "truck":
            return Truck(brand, photo_file_name, carrying, body_whl)
        elif car_type == "spec_machine":
            return SpecMachine(brand, photo_file_name, carrying, extra)
        else:
            return None
    except BaseException:
        return None


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)    # skip the header line
        for row in reader:
            # print(row)
            car = parse_row(row)
            if car is not None:
                car_list.append(car)
    return car_list


if __name__ == "__main__":
    result = get_car_list("coursera_week3_cars.csv")
    print(result)
    for car in result:
        print(car.get_photo_file_ext())
    # print(result[1].get_body_volume())


# import csv
# import os.path


# class CarBase():
#     """базовый класс для транспортных средств"""

#     # атрибут для хранения обязательных параметров класса, описывающего транспортное средство
#     required = []

#     def __init__(self, brand, photo_file_name, carrying):
#         self.brand = self.validate_input(brand)
#         self.photo_file_name = self.validate_photo_filename(photo_file_name)
#         self.carrying = float(self.validate_input(carrying))

#     def validate_input(self, value):
#         """метод валидации данных, возвращает значение, если оно валидно,
# иначе выбрасывает исключение ValueError"""
#         if value == '':
#             raise ValueError
#         return value

#     def validate_photo_filename(self, filename):
#         for ext in ('.jpg', '.jpeg', '.png', '.gif'):
#             if filename.endswith(ext) and len(filename) > len(ext):
#                 return filename
#         raise ValueError

#     def get_photo_file_ext(self):
#         _, ext = os.path.splitext(self.photo_file_name)
#         return ext

#     @classmethod
#     def create_from_dict(cls, data):
#         """создает экземпляр класса из словаря с параметрами"""
#         parameters = [data[parameter] for parameter in cls.required]
#         return cls(*parameters)


# class Car(CarBase):
#     """класс описывающий автомобили для перевозок людей"""
#     car_type = "car"
#     required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

#     def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
#         super().__init__(brand, photo_file_name, carrying)
#         self.passenger_seats_count = int(self.validate_input(passenger_seats_count))


# class Truck(CarBase):
#     """класс описывающий автомобили для перевозок грузов"""
#     car_type = "truck"
#     required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

#     def __init__(self, brand, photo_file_name, carrying, body_whl):
#         super().__init__(brand, photo_file_name, carrying)
#         self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)

#     def get_body_volume(self):
#         """возвращает объем кузова"""
#         return self.body_length * self.body_width * self.body_height

#     def parse_whl(self, body_whl):
#         """возвращает реальные размеры кузова length, width, height"""
#         try:
#             length, width, height = (float(c) for c in body_whl.split("x", 2))
#         except Exception:
#             length, width, height = 0.0, 0.0, 0.0
#         return length, width, height


# class SpecMachine(CarBase):
#     """класс описывающий спецтехнику"""

#     car_type = "spec_machine"
#     required = ['brand', 'photo_file_name', 'carrying', 'extra']

#     def __init__(self, brand, photo_file_name, carrying, extra):
#         super().__init__(brand, photo_file_name, carrying)
#         self.extra = self.validate_input(extra)


# def get_car_list(csv_filename):
#     """возвращает список объектов, сохраненных в файле csv_filename"""

#     car_types = {'car': Car, 'spec_machine': SpecMachine, 'truck': Truck}
#     csv.register_dialect('cars', delimiter=';')
#     car_list = []

#     with open(csv_filename, 'r') as file:
#         reader = csv.DictReader(file, dialect='cars')
#         for row in reader:
#             try:
#                 car_class = car_types[row['car_type']]
#                 car_list.append(car_class.create_from_dict(row))
#             except Exception:
#                 pass

#     return car_list


# if __name__ == '__main__':
#     pass
