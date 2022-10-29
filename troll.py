import random

player_health = 50
troll_health = 50

print("Вы вошли в тёмную пещеру. Внезапно, из темноты выпрыгивает ТРОЛЛЬ!")

while True:
    player_attack = random.randrange(10) + 1
    troll_health = troll_health - player_attack
    print("Игрок нападает. Сила атаки=" + str(player_attack) + ". У тролля осталось " + str(troll_health) + " жизней")

    if troll_health <= 0:
        print("Игрок победил! Ура!")
        break

    troll_attack = random.randrange(10) + 1
    player_health = player_health - troll_attack
    print("Тролль нападает. Сила атаки=" + str(troll_attack) + ". У игрока осталось " + str(player_health) + " жизней")

    if player_health <= 0:
        print("Тролль победил :(")
        break
    
    flee = input("Убегаем?  -> ")
    if flee == "да":
        print("Игрок убегает")
        break



