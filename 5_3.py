class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("такого этажа нет")
        else:
            for i in range(1, self.number_of_floors):
                print(i)
                i += 1
                if i > new_floor:
                    break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, floors):
        if isinstance(floors, int):
            return House(self.name, self.number_of_floors + floors)

    def __iadd__(self, floors):
        if isinstance(floors, int):
            self.number_of_floors += floors
            return self
        

    def __radd__(self, floors):
        return self.__add__(floors)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) 

h1 = h1 + 10 
print(h1)
print(h1 == h2)

h1 += 10  
print(h1)

h2 = 10 + h2  
print(h2)

print(h1 > h2)  
print(h1 >= h2)  
print(h1 < h2)  
print(h1 <= h2)  
print(h1 != h2)  
