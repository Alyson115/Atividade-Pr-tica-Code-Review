def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass
    N1 = string1.replace(" ", "").lower()
    N2 = string2.replace(" ", "").lower()
    O1 = sorted(N1)
    O2 = sorted(N2)
    return O1 == O2


def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado


def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
