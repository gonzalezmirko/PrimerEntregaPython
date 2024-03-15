import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
# max_attempts = 10
# Numero de errores maximo de errores
max_errors=5
# Contador de errores
cont=0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("Pero ten cuidado, si te equivocas ",max_errors," veces pierdes.")
word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while (cont != max_errors):
 # Pedir al jugador que ingrese una letra diferente a vacio ""
    letter = input("Ingresa una letra: ").lower()
    while (letter == "") :
        letter = input("Error, no se ingreso ninguna letra, vuelta a intentar: ").lower()
 # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
 # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
 # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        cont += 1
        print("!Cuidado! Cantidad de errores: ",cont)
        print("Lo siento, la letra no está en la palabra.")
 # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_errors} intentos.")
    print(f"La palabra secreta era: {secret_word}")