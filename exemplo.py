def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve apenas receber argumentos inteiros")
    try:
        aux = dividendo / divisor
    except:
        print(f"Não foi possível dividir {dividendo} por {divisor}")
        raise
    return aux

def testa_divisao(divisor):    
    resultado = dividir(10, divisor)
    print(f"10 / {divisor} = {resultado}")


# try:
#     testa_divisao(2.5)
# except Exception as e:
#     print(e)
# except ZeroDivisionError as e:
#     # print("Erro de disivão por zero tratado")
#     print("Erro divisão por zero")
# except Exception as e:
#     # print("Erro de atributo tratado")
#     print("Tratamento genérico")
# print(f"Programa Encerrado")

try:
    print("O fluxo está aqui <----")
    raise ValueError
except Exception:
    print("Agora ele foi para cá ---->")
print("E enfim, ele continua ...")