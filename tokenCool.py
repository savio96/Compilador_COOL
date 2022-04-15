

class TokenCool():
    def __init__(self):
        self.TK_IDENTIFICADOR=0
        self.TK_NUM=1
        self.TK_STRING=2
        self.TK_OPERADOR=3
        self.TK_PONTUACAO=4
        self.TK_ATRIBUICAO=5
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