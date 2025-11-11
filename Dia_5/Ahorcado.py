from random import choice
from typing import List, Tuple, Set

WORDS = [
    "mesa", "silla", "laptop", "ventana", "arbol", "departamento", "edificio",
    "docente", "ingenieria", "armario", "taquilla", "zapatilla", "tendedera",
    "arrocera", "telefono", "audifonos"
]
MAX_LIVES = 6


def pick_word() -> str:
    return choice(WORDS)


def reveal_letters(guess: str, word: str, display: List[str]) -> Tuple[List[str], bool]:
    """
    Marca en `display` las letras correctas encontradas por `guess`.
    Si guess es una letra, actualiza posiciones iguales.
    Si guess es la palabra completa, revela toda la palabra si coincide.
    Devuelve la nueva display y un booleano indicando si hubo acierto.
    """
    hit = False
    if len(guess) == 1:
        for i, ch in enumerate(word):
            if ch == guess:
                display[i] = ch
                hit = True
    else:
        # intento de adivinar la palabra completa
        if guess == word:
            for i, ch in enumerate(word):
                display[i] = ch
            hit = True
    return display, hit


def game_loop():
    lives = MAX_LIVES
    word = pick_word()
    display = ["_"] * len(word)
    used_letters: Set[str] = set()

    print("Bienvenido al Ahorcado")
    print(" ".join(display))

    while True:
        if lives <= 0:
            print("Te has quedado sin intentos :'(")
            print("GAME OVER!!!!")
            print(f"La palabra correcta era: {word}")
            break

        guess = input("Ingresa una letra o intenta adivinar la palabra: ").strip().lower()

        if not guess:
            print("No ingresaste nada. Intenta de nuevo.")
            continue

        if not guess.isalpha():
            print("Entrada inválida: solo letras (sin espacios ni números).")
            continue

        # si es una letra simple
        if len(guess) == 1:
            if guess in used_letters:
                print(f"Ya intentaste la letra '{guess}'. Letras usadas: {', '.join(sorted(used_letters))}")
                print(" ".join(display))
                continue

            used_letters.add(guess)
            display, hit = reveal_letters(guess, word, display)
            if not hit:
                lives -= 1
                print(f"Letra incorrecta. Vidas restantes: {lives}")
            else:
                print("¡Acertaste una letra!")
        else:
            # intento de adivinar la palabra completa
            if guess in used_letters:
                # opcional: tracking de intentos de palabra completa también en used_letters
                print(f"Ya intentaste '{guess}' antes.")
            else:
                used_letters.add(guess)
                display, hit = reveal_letters(guess, word, display)
                if not hit:
                    lives -= 1
                    print(f"Palabra incorrecta. Vidas restantes: {lives}")
                else:
                    print("¡Has adivinado la palabra completa!")

        current = "".join(display)
        print(f"{current} | Vidas restantes: {lives}")

        if "_" not in display:
            print("¡Has ganado! 🎉")
            print(f"Respuesta: {current}")
            break


if __name__ == "__main__":
    game_loop()