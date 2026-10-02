def to_binary(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2

    return binario
#danie nigger
