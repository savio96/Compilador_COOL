from analisadorLexico import AnalisadorLexico
from analisadorSintatico import AnalisadorSintatico
from analisadorSemantico import AnalisadorSemantico
# Ler e fechar arquivo e retorna o conteúdo.
def lerArquivo(nomeArq):
    arq = open(nomeArq, "r")
    string = arq.read()
    arq.close()
    return string

# Função principal
def main(self=None):
    #arq=lerArquivo("coolHello.txt")
    # Analisador Léxico
    #analisarLexico=AnalisadorLexico(arq)
    #print(analisarLexico.proxToken())
    #print("\n")
    #analisadorSintatico=AnalisadorSintatico("coolCells.txt")
    #analisadorSintatico.exec("coolCells.txt")
    analisadorSemantico=AnalisadorSemantico("exam.txt")
    analisadorSemantico.exec()

main()

