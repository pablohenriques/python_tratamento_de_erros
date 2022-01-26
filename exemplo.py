def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo / divisor

def testa_divisao(divisor):
    try:
        resultado = dividir(10, divisor)
        print(f"10 / {divisor} = {resultado}")
    except ZeroDivisionError:
        print("Erro de disivão por zero tratado")
    except AttributeError:
        print("Erro de atributo tratado")

try:
    testa_divisao(0)
except AttributeError:
    print("Erro de atributo tratado")

print(f"Programa Encerrado")