import json

# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        """
        Конструктор базового класса Animal.
        :param name: Имя животного.
        :param age:  Возраст животного.
        """
        self.name = name
        self.age = age

    def make_sound(self):
        """
        Базовый метод для звука, который издает животное.
        Если не переопределить в подклассе, вывод будет "Some sound".
        """
        return "Some sound"

    def eat(self):
        """
        Базовый метод для обозначения того, что животное ест.
        """
        print(f"{self.name} is eating.")

    def to_dict(self):
        """
        Преобразует объект Animal в словарь.
        Этот словарь потом будет сохранён в JSON-файле.
        """
        return {
            "type": "animal",  # Обозначаем тип (если вдруг нужен)
            "name": self.name,
            "age": self.age
        }


# 2. Подклассы (Bird, Mammal, Reptile), которые наследуют от Animal.

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        """
        Конструктор подкласса Bird, добавляет размах крыльев (wing_span).
        """
        super().__init__(name, age)  # Вызов конструктора родителя
        self.wing_span = wing_span

    def make_sound(self):
        """
        Переопределение звука, который издает птица.
        """
        return "Tweet"

    def fly(self):
        """
        Дополнительный метод, уникальный для птиц: они могут летать.
        """
        print(f"{self.name} is flying.")

    def to_dict(self):
        """
        Преобразует объект Bird в словарь (для сохранения в JSON).
        Обязательно указываем 'type': 'bird', чтобы при загрузке
        создать именно Bird.
        """
        return {
            "type": "bird",
            "name": self.name,
            "age": self.age,
            "wing_span": self.wing_span
        }


class Mammal(Animal):
    def __init__(self, name, age, fur_type):
        """
        Конструктор подкласса Mammal, добавляет fur_type (тип шерсти).
        """
        super().__init__(name, age)
        self.fur_type = fur_type

    def make_sound(self):
        """
        Переопределение звука, который издает млекопитающее.
        """
        return "Roar"

    def walk(self):
        """
        Дополнительный метод, уникальный для млекопитающих: они могут ходить.
        """
        print(f"{self.name} is walking.")

    def to_dict(self):
        """
        Преобразует объект Mammal в словарь.
        """
        return {
            "type": "mammal",
            "name": self.name,
            "age": self.age,
            "fur_type": self.fur_type
        }


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        """
        Конструктор подкласса Reptile, добавляет scale_type (тип чешуи).
        """
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        """
        Переопределение звука, который издает рептилия.
        """
        return "Hiss"

    def crawl(self):
        """
        Дополнительный метод, уникальный для рептилий: они могут ползать.
        """
        print(f"{self.name} is crawling.")

    def to_dict(self):
        """
        Преобразует объект Reptile в словарь.
        """
        return {
            "type": "reptile",
            "name": self.name,
            "age": self.age,
            "scale_type": self.scale_type
        }


# Функция для восстановления (создания) объекта животного из словаря:
def create_animal(animal_data):
    """
    На вход подаётся словарь (например, {"type": "bird", "name": "Parrot", "age": 2, "wing_span": 25}).
    Функция создает правильный объект (Bird, Mammal, Reptile или Animal) на основе 'type'.
    """
    animal_type = animal_data["type"]  # bird / mammal / reptile / ...
    name = animal_data["name"]
    age = animal_data["age"]

    if animal_type == "bird":
        return Bird(name, age, animal_data["wing_span"])
    elif animal_type == "mammal":
        return Mammal(name, age, animal_data["fur_type"])
    elif animal_type == "reptile":
        return Reptile(name, age, animal_data["scale_type"])
    else:
        # Если type не распознан, возвращаем базовый Animal
        return Animal(name, age)


# Функция демонстрации полиморфизма:
def animal_sound(animals):
    """
    Принимает список объектов-животных и вызывает метод make_sound() у каждого.
    Показывает, что у каждого класса свой звук.
    """
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")


# 3. Классы сотрудников зоопарка (ZooKeeper, Veterinarian)
class ZooKeeper:
    def __init__(self, name):
        """
        Сотрудник зоопарка (смотритель).
        """
        self.name = name

    def feed_animal(self, animal):
        """
        Метод кормления животного.
        """
        print(f"{self.name} is feeding {animal.name}.")

    def to_dict(self):
        """
        Преобразование в словарь (для сохранения в JSON).
        """
        return {
            "role": "zookeeper",
            "name": self.name
        }


class Veterinarian:
    def __init__(self, name):
        """
        Сотрудник зоопарка (ветеринар).
        """
        self.name = name

    def heal_animal(self, animal):
        """
        Метод лечения животного.
        """
        print(f"{self.name} is healing {animal.name}.")

    def to_dict(self):
        """
        Преобразование в словарь (для сохранения в JSON).
        """
        return {
            "role": "veterinarian",
            "name": self.name
        }


# Вспомогательная функция для восстановления объектов сотрудников:
def create_staff(staff_data):
    """
    На вход ожидается словарь вида {"role": "zookeeper", "name": "Alice"} или {"role": "veterinarian", "name": "Bob"}.
    Функция создает правильный объект (ZooKeeper или Veterinarian) на основе 'role'.
    """
    role = staff_data["role"]
    name = staff_data["name"]
    if role == "zookeeper":
        return ZooKeeper(name)
    elif role == "veterinarian":
        return Veterinarian(name)
    else:
        raise ValueError(f"Unknown staff role: {role}")


# 4. Класс Zoo (композиция: в зоопарке есть животные и сотрудники).
class Zoo:
    def __init__(self, name):
        """
        Инициализируем зоопарк с заданным именем.
        Здесь хранится список объектов-животных (self.animals) и
        список объектов-сотрудников (self.staff).
        """
        self.name = name
        self.animals = []  # Сюда добавляем Bird, Mammal, Reptile и т.д.
        self.staff = []    # Сюда добавляем ZooKeeper, Veterinarian и т.д.

    def add_animal(self, animal):
        """
        Добавляет объект животного в зоопарк.
        """
        self.animals.append(animal)

    def add_staff(self, staff_member):
        """
        Добавляет сотрудника в зоопарк.
        """
        self.staff.append(staff_member)

    def list_animals(self):
        """
        Возвращает список ИМЁН (str) всех животных.
        """
        return [animal.name for animal in self.animals]

    def list_staff(self):
        """
        Возвращает список ИМЁН (str) всех сотрудников.
        """
        return [staff_member.name for staff_member in self.staff]


# 5. Класс ZooWithStorage — расширяет Zoo, добавляя методы сохранения/загрузки.
class ZooWithStorage(Zoo):
    def save_zoo_state(self, filename):
        """
        Сохраняем все данные о зоопарке (имя, животные, сотрудники) в формат JSON.
        При этом у каждого животного и сотрудника вызываем метод to_dict().
        """
        zoo_data = {
            "name": self.name,
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [member.to_dict() for member in self.staff]
        }
        with open(filename, "w", encoding="utf-8") as file:
            # Записываем JSON-файл с отступами в 4 пробела (indent=4)
            json.dump(zoo_data, file, ensure_ascii=False, indent=4)
        print(f"Zoo state saved to {filename}.")

    def load_zoo_state(self, filename):
        """
        Загружаем данные из файла JSON, восстанавливаем:
         - self.name (имя зоопарка)
         - self.animals (полноценные объекты Bird/Mammal/Reptile/Animal)
         - self.staff (объекты ZooKeeper/Veterinarian)
        """
        with open(filename, "r", encoding="utf-8") as file:
            zoo_data = json.load(file)
            # 1) Восстанавливаем имя зоопарка
            self.name = zoo_data["name"]
            # 2) По каждому словарю в zoo_data["animals"] создаем полноценное животное
            self.animals = [create_animal(animal_dict) for animal_dict in zoo_data["animals"]]
            # 3) По каждому словарю в zoo_data["staff"] создаем объект сотрудника
            self.staff = [create_staff(staff_dict) for staff_dict in zoo_data["staff"]]
        print(f"Zoo state loaded from {filename}.")


# 6. Демонстрация работы
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = ZooWithStorage("Wildlife Park")

    # Создаем животных
    parrot = Bird("Parrot", 2, 25)
    lion = Mammal("Lion", 5, "Short Fur")
    snake = Reptile("Snake", 3, "Scales")

    # Создаем сотрудников
    zookeeper = ZooKeeper("Alice")
    veterinarian = Veterinarian("Bob")

    # Добавляем в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Действия сотрудников
    zookeeper.feed_animal(parrot)
    veterinarian.heal_animal(snake)

    # Сохраняем текущее состояние зоопарка в файл
    # (после этого в папке появится файл zoo_state.json с правильными словарями)
    zoo.save_zoo_state("zoo_state.json")

    # Создаем новый зоопарк и загружаем в него данные из файла
    new_zoo = ZooWithStorage("New Park")  # имя зоопарка временно
    new_zoo.load_zoo_state("zoo_state.json")  # тут будет восстановлено правильное имя
    print(f"Zoo name: {new_zoo.name}")
    print(f"Animals: {new_zoo.list_animals()}")
    print(f"Staff: {new_zoo.list_staff()}")

