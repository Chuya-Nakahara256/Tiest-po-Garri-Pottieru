print('Кто ты из фильма "Гарри Поттер и тайная комната". Отвечай на вопросы и узнаешь, на кого ты больше похож!')

potter_points = 0

question1 = "Ты любишь змей?"

question2 = "Ведёшь ли ты дневник?"

question3 = "Кто ползает по трубам? Про кого ты первым подумал?"

question4 = "Есть ли у тебя своя комната?"

question5 = "Мечтаешь ли ты о величии?"

print(question1)
print("1. Да. 2. Нет.")
answer1 = input("Введите ответ цифрой: ")
if answer1 == "1":
  potter_points += 1
else:
  potter_points += 0
  
print(question2)
print("1. Да. 2. Нет.")
answer2 = input("Введите ответ цифрой: ")
if answer2 == "1":
  potter_points += 1
else:
  potter_points += 0
  
print(question3)
print("1. Про Василиска. 2. Про трубочиста.")
answer3 = input("Введите ответ цифрой: ")
if answer3 == "1":
  potter_points += 1
else:
  potter_points += 0
  
print(question4)
print("1. Да. 2. Нет.")
answer4 = input("Введите ответ цифрой: ")
if answer4 == "2":
  potter_points += 1
else:
  potter_points += 0
  
print(question5)
print("1. Да. 2. Нет.")
answer5 = input("Введите ответ цифрой: ")
if answer5 == "1":
  potter_points += 1
else:
  potter_points+= 0
  
if potter_points >= 3:
  
  print('Из фильма "Гарри Поттер и тайная комната" ты определённо сам Том Реддл! Такой же хитрый и коварный')
else:
  print('Из фильма "Гарри Поттер и тайная комната" ты сам Гарри Поттер! Храбрый и честный человек')
