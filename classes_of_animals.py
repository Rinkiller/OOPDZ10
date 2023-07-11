# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    name:str
    weigth:int
    age:int
    def __init__(self , name:str = None, weigth:int = 0, age:int = 0) -> None:
        self.name = name
        self.weigth = weigth
        self.age = age
    def get_spicific_atributes_of_class(self) -> str:
        print(f'Специфические особенности: ')

class Fish(Animal):
    freshwater:bool
    cartilaginous_fish:bool
    scales:bool
    def __init__(self , name:str , weigth:int , age:int , freshwater:bool = True , cartilaginous_fish:bool = True , scales:bool = True ) -> None:
        self.freshwater = freshwater        # пресноводная
        self.cartilaginous_fish = cartilaginous_fish    # хрящевая рыба  (bone fish)
        self.scales = scales    # чешуя 
        super().__init__( name , weigth , age)
    def get_spicific_atributes_of_class(self) -> str:
        return f'{self.freshwater = } , {self.cartilaginous_fish = } , {self.scales = }'
    

class Birds(Animal):
    warm_blooded = True     # теплокровное
    plumage = True          # перья
    beak = True             # клюв
    def __init__(self , name , weigth , age ) -> None:
        super().__init__(name , weigth , age)
    def get_spicific_atributes_of_class(self) -> str:
        return f'{self.warm_blooded = } , {self.plumage = } , {self.beak = }'
    

class Elephant(Animal):
    trunk = True # хобот
    tusks = True # бивни
    type_of_elephant: str                #Саванный слон Лесной слон Индийский слон Суматранский слон Цейлонский слон Борнейский слон
    def __init__(self , name , weigth , age , type_of_elephant) -> None:
        self.type_of_elephant = type_of_elephant
        super().__init__( name , weigth , age)
    def get_spicific_atributes_of_class(self) -> str:
        return f'{self.trunk = } , {self.tusks = } , {self.type_of_elephant = }'

# Урок 10. ООП. Начало
# 📌Доработаем задачи 5-6. Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Factori:
    cls:object
    __list_of_save_classes = []
    def Give_me_a_new_element(self, other , *args , **kwargs) -> object:
        rezult = other(*args , **kwargs)
        self.__list_of_save_classes.append(other)
        return rezult
    def print_list_of_save_classes(self):
        return self.__list_of_save_classes
    
f = Factori()
el = f.Give_me_a_new_element(Elephant , 'fgdrg' , 890 , 12 , 'Лесной слон')
print(el.get_spicific_atributes_of_class())
print(f.print_list_of_save_classes)
