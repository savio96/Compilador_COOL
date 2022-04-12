from analisadorLexico import Analisador

def lerArquivo(nomeArq):
    arq = open(nomeArq, "r")
    string = arq.read()
    arq.close()

    return string


def main(self=None):
    arq=lerArquivo("teste.txt")

    analisar=Analisador(arq)
    print(analisar.proxToken())
    #teste=Analisador.ehNumero(self,"b")
    #teste=Analisador.ehDigito(self,"1")
    #teste=Analisador.ehOperador(self,"3")
    #print(teste)


main()