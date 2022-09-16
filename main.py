# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia

print("Bienvenido a mi trivia sobre: Conocimiento general ")

# Es importante dar instrucciones sobre cómo jugar:
print(
    "Tienes dos oportunidades en cada pregunta. Si respondes correctamente pasaras a la siguiente pregunta.\nTendras que escribir la letra de la respuesta que crees correcta y darle click en ENTER ")
print("Al final te mostremos el puntaje obtenido \n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
r1 = 'b'
r2 = 'c'
r3 = 'c'
r4 = 'a'
r5 = 'd'

# Pregunta 1
print("1) ¿Quién fue el creador de windows?\n")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie")
print("\n")

respuesta_1 = input("Ingresa tu respuesta: ")

if respuesta_1 != r1:
    print("Te queda una oportunidad, vuelve a intentarlo")
    respuesta_1 = input("Ingresa tu respuesta: \n")
else:
    print("Respuesta correcta\n")

# Pregunta 2
print("\n2) ¿Cuantas franjas tiene la bandera de Estados Unidos?\n")
print("a) 18")
print("b) 52")
print("c) 13")
print("d) 8")

respuesta_2 = input("Tu respuesta: ")

if respuesta_2 != r2:
    print("Te queda una oportunidad, vuelve a intentarlo")
    respuesta_2 = input("Ingresa tu respuesta: ")
else:
    print("Respuesta correcta")
print("\n")

# Pregunta 3
print("\n3) ¿A que equipo de fútbol se le conoce como Los diablos rojos?\n")
print("a) Manchester City")
print("b) Liverpool")
print("c) Manchester United")
print("d) Arsenal")

respuesta_3 = input("Tu respuesta: ")

if respuesta_3 != r3:
    print("Te queda una oportunidad, vuelve a intentarlo")
    respuesta_3 = input("Ingresa tu respuesta: ")
else:
    print("Respuesta correcta")
print("\n")

# Pregunta 4
print("\n4) ¿En qué año se fundó Netflix: 1997, 2001, 2009, 2015?\n")
print("a) 1997")
print("b) 2001")
print("c) 2009")
print("d) 2015")

respuesta_4 = input("Tu respuesta: ")

if respuesta_4 != r4:
    print("Te queda una oportunidad, vuelve a intentarlo")
    respuesta_4 = input("Ingresa tu respuesta: ")
else:
    print("Respuesta correcta")
print("\n")

# Pregunta 5
print("\n5) ¿Cuántos días le toma a la tierra dar una vuelta a la órbita del sol?\n")
print("a) 1")
print("b) 240")
print("c) 180")
print("d) 365")

respuesta_5 = input("Tu respuesta: ")

if respuesta_5 != r5:
    print("Te queda una oportunidad, vuelve a intentarlo")
    respuesta_5 = input("Ingresa tu respuesta: ")
else:
    print("Respuesta correcta")
print("\n")

correctas = 0
if respuesta_1 == r1:
    correctas += 1
if respuesta_2 == r2:
    correctas += 1
if respuesta_3 == r3:
    correctas += 1
if respuesta_4 == r4:
    correctas += 1
if respuesta_5 == r5:
    correctas += 1

print("Tu puntaje es :", correctas*20, "con ", correctas, "preguntas correctas. ")

