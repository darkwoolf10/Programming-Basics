#
# Тестова програма для демонстрації роботи функцій і та деяких
# простих маніпуляцій зі змінними
# в цілях домашього завдання курсу основи програмування
# Автор програми Богдан Прокопенко
# 

# Підключення модул`s os, sys
import os, sys


name = input ("Привет меня зовут Т-800.\n" +
              "Я старый, но не бесполезный \n" +
              "А как тебя зовут?\n")
print("Привет ", name + "\n")

print('Какая у тебя фамилия?\n')
surname = input()

print("Приятно познакомиться " + name +" "+ surname + "\n" +
      "Какого ты года рождения?\n")
birth_age = input()

print("B каком часу ты просыпаешься?\n")
hour = input ()

print(name, "как ты думаешь: чем можно работать?\n")
equip = input ()

print(name," назови любой бытовой прибор?)\n")
pribor = input ()

print(name," напиши пожалуйста название своей любимой вещи?\n")
liked = input()

print("Хорошо " ,name, " теперь укажи свое любимое число?\n")
like_numb = input()

print ("Спасибо ",name," теперь назови свой любимый город?\n" )
like_city = input()

print (name, " ты наверняка ругаешься, какое твое любимое ругательство?\n")
fuck_word = input()

print (name, " какая часть тела человека тебя привлекает больше всего?\n")
hum_part = input()

print (name, " исходя из нашей беседы я сделал выводы...\n")


print("В " + birth_age +" году в "+ hour + " на посольство Нигерии было совершено нападение приступниками, \n"+
      " вооружёнными "+ equip + "\n"
      " Были украдены " + pribor +" и "+ liked + "\n"
      " Как сообщает пресса, приступников было "+ like_numb + "\n"
      " Из них был распознан только " + name +" "+ surname + "\n"
      " Как стало известно, преступники направились в город " + like_city + "\n"
      " Из посольства выбежали охранники с криками " + fuck_word + "\n"
      " и открыли огонь по убегавшим. Одному они попали в " + hum_part + "\n")

resume = ("В " + birth_age +" году в "+ hour + " на посольство Нигерии было совершено нападение приступниками, \n"+
      " вооружёнными "+ equip + "\n"
      " Были украдены " + pribor +" и "+ liked + "\n"
      " Как сообщает пресса, приступников было "+ like_numb + "\n"
      " Из них был распознан только " + name +" "+ surname + "\n"
      " Как стало известно, преступники направились в город " + like_city + "\n"
      " Из посольства выбежали охранники с криками " + fuck_word + "\n"
      " и открыли огонь по убегавшим. Одному они попали в " + hum_part + "\n")

 

input (name + ", давай сохраним нашу беседу в отделный файл? \n" +
       "Для продолжения нажми Enter ")
print ("Введите путь для сохранния файла ")

# Путь который указывает пользователь для сохранения файла 
user_pass = input ()

#Создание дирректории по заданному пользователем пути
os.makedirs (user_pass)

# изменение рабочей дирректории на заданную пользователем
os.chdir (user_pass)

print("Введите имя файла \n")

# файл будет создан под именем который укажет пользователь
file_name = input()

# with управляет контекстом создаваемого файлового объекта f,
# избавляя от необходимости вручную закрывать файл.
# Метод write принимает строку. Для того, чтобы привести какое-то значение к строковому виду,
# используются функции str, repr и метод format класса str
with open(file_name + ".txt", 'w', encoding='utf-8') as f:
	print(resume, file=f)

print (name + " наш диалог ты сможешь найти по пути " + user_pass + file_name + ".txt")

input ("Что бы выйти нажмите Еnter")
