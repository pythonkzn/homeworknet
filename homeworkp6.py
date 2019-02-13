import copy
class Animals:
    weight = 0
    name = ''
    nickname = ''
    voice = ''
    eaten = False


    def __init__(self, weight, name, nickname, voice, eaten):
        self.weight = weight
        self.name = name
        self.nickname = nickname
        self.voice = voice
        self.eaten = False


    def feed(self):
        self.eaten = True


class Milk_animals(Animals): #класс животных дающих молоко
    milked = False
    def milk(self):
        self.milked = True

class Wool_animals(Animals): #класс животных дающих шерсть
    have_cut = False
    def cut(self):
        self.have_cut = True

class Birds(Animals): #класс птиц
    egg_got = False
    def get_eggs(self):
        self.egg_got = True

milk_animal_list =[]
bird_list =[]
wool_animal_list =[]
animal_list = []
#создаем экземпляр для каждого животного

goose1 = Birds(10,'Гусь','Серый','Га-га', 'False')
bird_list.append(goose1)
animal_list.append(goose1)

goose2 = Birds(10,'Гусь','Белый','Га-га', 'False')
#rec = copy.deepcopy(goose2)
bird_list.append(goose2)
animal_list.append(goose2)

cow = Milk_animals(400,'Корова','Манька','Мууу', 'False')
milk_animal_list.append(cow)
animal_list.append(cow)

sheep1 = Wool_animals(50,'Овца','Барашек','Бэээ', 'False')
wool_animal_list.append(sheep1)
animal_list.append(sheep1)

sheep2 = Wool_animals(50,'Овца','Кудрявый','Бэээ', 'False')
wool_animal_list.append(sheep2)
animal_list.append(sheep2)

chicken1 = Birds(5,'Курица','Ко-ко','Ко-ко', 'False')
bird_list.append(chicken1)
animal_list.append(chicken1)

chicken2 = Birds(4,'Курица','Кукареку','Ко-ко', 'False')
bird_list.append(chicken2)
animal_list.append(chicken2)

goat1 = Wool_animals(30,'Коза','Рога','Мэээ', 'False')
milk_animal_list.append(goat1)
animal_list.append(goat1)

goat2 = Wool_animals(30,'Коза','Копыта','Мэээ', 'False')
milk_animal_list.append(goat2)
animal_list.append(goat2)

duck = Birds(6,'Утка','Кряква','Кря-кря', 'False')
bird_list.append(duck)
animal_list.append(duck)

sum_weight_birds = 0
sum_weight_milks = 0
sum_weight_wools = 0

i = 0
for bird in bird_list:
    Animals.feed(bird) #покормили птиц
    Birds.get_eggs(bird) #собрали яйца
    sum_weight_birds += bird_list[i].weight
    i +=1
i = 0
for milk in milk_animal_list:
    Animals.feed(milk) #покормили молочных животных
    Milk_animals.milk(milk) #собрали яйца
    sum_weight_birds += milk_animal_list[i].weight
    i +=1
i = 0
for wool in wool_animal_list:
    Animals.feed(wool) #покормили шерстяных животных
    Wool_animals.cut(wool) #постригли шерсть
    sum_weight_wools += wool_animal_list[i].weight
    i +=1

weight = sum_weight_birds + sum_weight_milks + sum_weight_wools

i = 0
max = 0
ind_max = 0

while i <= (len(animal_list)-2):
    if int(animal_list[i].weight) >= max:
        ind_max = i
        max = int(animal_list[i].weight)
    i += 1


print('Общий вес {} кг'.format(weight))
print('Самый большой вес у животного {} '.format(animal_list[ind_max].name))











