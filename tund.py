import random
v = 0
d=int(input("Поиграем в камень, ножницы, бумага? 1 - да , 0 - нет " ))
if d==1:
    while (v == 0):
            a = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            if (a == 1 or a == 2 or a == 3):
                v = 1   
    if a == 1:
            print("Камень.")  
    if a == 2:
            print("Ножницы.") 
    if a == 3:
            print("Бумага.")  
    c = random.randint(1, 3)
    if c == 1:
            print("Противник выбрал камень.") 
    if c == 2:
            print("Противник выбрал ножницы.")
    if c == 3:
            print("Противник выбрал бумагу.")
    if a == c:
            win = 0
    if a == 1 and c == 2:
            win = 1 
    if a == 1 and c == 3:
            win = 2 
    if a == 2 and c == 1:
            win = 2  
    if a == 2 and c == 3:
            win = 1 
    if a == 3 and c == 1:
            win = 1
    if a == 3 and c == 2:
            win = 2
    if win == 0:
            print("Ничья!")
            print("Победишь в следуйщий раз")
    if win == 1:
            print("Победа!")
    if win == 2:
            print("Поражение!")
            print("Победишь в следуйщий раз")