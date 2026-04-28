dicc = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "-..",
    " " : "/"
}

def abc_to_morse(sent):
    message = ""
    for letter in sent:
        if len(message) != 0:
            if letter != " ": message = f"{message}/"
        message = f"{message}{dicc.get(letter)}"

    return message


def morse_to_abc(sent):
    message = ""
    count = 0
    sent = sent.split("/")
    print(sent)
    for code in sent:
        print(code)
        for key,value in dicc.items():
            if value == code:
                message = f"{message}{key}"
            if code == "":
                message = f"{message}{" "}"

    print(message)





mess = input("Digite el mensaje: ").lower()

morse_to_abc(mess)
