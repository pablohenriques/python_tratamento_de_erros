class LeitorDeArquivo:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        #raise FileNotFoundError
        print(f"Abrindo arquivo: {self.arquivo}")

    def ler_proximo_linha(self):
        raise IOError
        print("Lendo linha ...")
        return "Linha do Arquivo"

    def fechar(self):
        print("Fechando arquivo")

    def __enter__(self):
        return self
    
    def __exit__(self, type, valor, traceback):
        print("Fechando aquivo")
