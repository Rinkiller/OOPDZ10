# напишите класс для хранения информации о человеке
# ФИО возраст и тд
# у класса должны быть методы birthday для увеличени возраста на год
# full_name для вывода полного имени
# убедитесь что свойство возраст надоступно для прямого изменения,
# но есть возможность получить текущий возраст
import random


class Human:
    first_name:str
    name:str
    last_name:str
    __age:int
    weigth:int
    def __init__(self , first_name:str , name:str , last_name:str , age:int , weiath:int ) -> None:
        self.first_name = first_name.title()
        self.name = name.title()
        self.last_name = last_name.title()
        self.__age = age
        self.weigth = weiath
    
    def full_name(self) -> str:
        return self.first_name + ' ' + self.name + ' ' + self.last_name
    
    def birthday(self) -> None:
        self.__age += 1
    
    def get_age(self) -> int:
        return self.__age


rin = Human('ilkin' , 'rin' , 'Firdaysow' , 38 , 75)
print(rin.get_age())
rin.birthday()
print(rin.get_age())
print(rin.full_name())
#print(rin.__age)   #AttributeError: 'Human' object has no attribute '__age'

# создайте класс сотрудник на основе класса человек
# У сотрудника должен быть шестизначный индентификационный номер, уровень доступа
# вычисляемый как остаток от деления суммы цифр id на 7

class Worker(Human):
    id:int
    
    
    def __init__(self, first_name: str, name: str, last_name: str, age: int, weiath: int , id:int=0) -> None:
        if len(str(id)) != 6:
            self.id = random.randint(100000 , 999999)
        else: 
            self.id = id
        # proxy = sum(list(map(int , str(self.id))))
        # self.level = proxy % 7
        # if self.level == 0 : self.level = 1
        super().__init__(first_name, name, last_name, age, weiath)

    @property # Защищает от изменений, делает из метода атрибут
    def acess_level(self) -> int:
        proxy = sum(list(map(int , str(self.id))))
        level = proxy % 7
        if level == 0 : level = 1
        return level

work1 = Worker('pior' , 'sdf' , 'dxgxdg' , 45 , 89 , 111112)
print(work1.acess_level)
print(work1.full_name())

