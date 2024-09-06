class House:
    houses_history = [] 

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  
        cls.houses_history.append(args[0])  
        return instance 

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа нет")
        else:
            for i in range(1, self.number_of_floors + 1):
                print(i)
                if i == new_floor:
                    break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __iadd__(self, other: int):
        return self.__add__(other)

    def __radd__(self, floors):
        return self.__add__(floors)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history) 

h2 = House('ЖК Акация', 20)
print(House.houses_history)  

h3 = House('ЖК Матрёшки', 30)
print(House.houses_history)  


del h2
del h3


print(House.houses_history)  
