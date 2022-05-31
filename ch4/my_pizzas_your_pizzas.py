# 4.11 Exercise
pizzas = ['calabresa','quatro queijos','muzzarela']
for pizza in pizzas:
        print(f"Eu gosto de pizza de {pizza}.")
print("Eu gosto muito de pizza!")

friend_pizzas = pizzas[:]
pizzas.append('atum')
friend_pizzas.append('portuguesa')

print(pizzas)
print(friend_pizzas)

print(f"Minhas pizzas favoritas são de {pizzas}")
print(f"As pizzas favoritas do meu amigo são de {friend_pizzas}")