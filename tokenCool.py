

class TokenCool():
    def __init__(self):
        self.TK_IDENTIFICADOR=0
        self.TK_NUM=1
        self.TK_STRING=2
        self.TK_OPERADOR_ARITIMETICO = 3
        self.TK_PONTUACAO=4
        self.TK_ATRIBUICAO=5
        self.TK_PALAVRARESERVADA=6
        self.TK_DELIMITADOR=7
        self.TK_OPERADOR_RELACIONAL=8
        self.TK_TIPO=9
        self.tipo = -1
        self.texto=""


    def getTipo(self):
        return self.tipo

    def setTipo(self,tipo):
        self.tipo=tipo

    def getTexto(self):
        return self.texto

    def setTexto(self,texto):
        self.texto=texto

    def mostrarToken(self,estado, texto):
        if estado==2:
            print("Token: "+texto + ": ",self.TK_IDENTIFICADOR)
        if estado==4 :
            print("Token: " + texto + ": ", self.TK_NUM)
        if estado==6:
            print("Token: " + texto + ": ", self.TK_STRING)
        if estado==8:
            print("Token: " + texto + ": ", self.TK_OPERADOR_ARITIMETICO)
        if estado == 10:
            print("Token: " + texto + ": ", self.TK_PALAVRARESERVADA)
        if estado == 12:
            print("Token: " + texto + ": ", self.TK_OPERADOR_RELACIONAL)
        if estado == 13:
            print("Token: " + texto + ": ", self.TK_ATRIBUICAO)
        if estado == 17:
            print("Token: " + texto + ": ", self.TK_DELIMITADOR)
        if estado == 22:
            print("Token: " + texto + ": ", self.TK_TIPO)