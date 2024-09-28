class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self,model,vin,numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.vin = vin
        if self.__is_valid_numbers:
            self.numbers = numbers


    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('некорретный тип vin номера')

        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('неверный диапазон vin номера')
            
        return True
    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers,str):
                raise IncorrectCarNumbers("Некорректный ти данных для номеров")
        if len(numbers) != 6:
                raise IncorrectCarNumbers("Неверная длина номера")
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет  номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')