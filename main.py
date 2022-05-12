from analisadorLexico import AnalisadorLexico

# Ler e fechar arquivo e retorna o conteúdo.
def lerArquivo(nomeArq):
    arq = open(nomeArq, "r")
    string = arq.read()
    arq.close()
    return string

# Função principal
def main(self=None):
    arq=lerArquivo("coolHello.txt")
    # AnalisadorLexico Léxico
    analisar=AnalisadorLexico(arq)
    print(analisar.proxToken())
    print("\n")

main()