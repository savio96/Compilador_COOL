import tokenCool
import string
from tokenCool import TokenCool


class Analisador(TokenCool):
    def __init__(self, conteudo):
        super().__init__()
        self.conteudo = conteudo
        self.estado = 0
        self.tokenC = TokenCool()

    def proxToken(self):
        atualChar = self.conteudo[0]
        palavra = ""
        estado = 0
        loop = True
        pos = 0
        contString=0
        contComent=0
        contComentMult=0
        # print(len(self.conteudo))

        while (loop == True):
            if estado == 0:
                if self.ehCharMin(atualChar):
                    estado = 1

                elif self.ehNumero(atualChar):
                    estado = 3

                elif self.ehEspaco(atualChar):
                    estado = 0

                elif self.ehString(atualChar):
                    estado = 5

                elif self.alertaComentarioMenos(atualChar):
                    estado=7
                #elif self.alertaComentarioMult(atualChar):
                    #pass

                elif self.ehOperadorRel(atualChar):
                    if atualChar=="<":
                        estado=11
                    elif atualChar=="~":
                        estado=18
                    else:
                        estado=15

                elif self.ehOperadorArit(atualChar):
                    estado=19

                elif self.ehDelimitador(atualChar) or self.ehDelimitadorEspe(atualChar):
                    estado=16
                elif self.ehCharMax(atualChar):
                    estado=20
            if estado == 1:
                if self.ehCharMin(atualChar) or self.ehCharMax(atualChar) or self.ehNumero(atualChar) or atualChar == "_":
                    estado = 1
                    palavra += atualChar
                    # atualChar = self.proxChar(pos)
                    # pos+=1

                else:
                    if self.palavrasReservadas(palavra):
                        estado=10
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                    else:
                        estado = 2
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
            if estado == 3:
                if self.ehNumero(atualChar):
                    estado = 3
                    palavra += atualChar
                elif not self.ehNumero(atualChar) and estado == 3 and not self.ehEspaco(atualChar):
                    raise Exception('Numero Desconhecido')
                else:
                    estado = 4
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado = 0
                    palavra = ""
            if estado == 5:
                if atualChar=="\\":
                    palavra=palavra
                else:
                    palavra+=atualChar

                if atualChar=='"' and contString==1:
                    estado=6
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado=0
                    palavra=""
                    contString=0
                else:
                    contString = 1

            if estado==7:
                if atualChar=="-":
                    contComent+=1
                if contComent==1 and not atualChar=="-":
                    atualChar=self.voltar(pos)
                    pos-=1
                    palavra+=atualChar
                    estado = 8
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra=""
                    estado=0
                # colocar os erros do cometários
                if contComent>=4:
                    estado=0
            """
            if estado==9:
                contComentMult+=1
                if not atualChar=="*" and contComentMult==1:
            """
            if estado==11:
                palavra += atualChar
                if atualChar=="=":
                    estado=12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra=""
                    estado=0
                elif atualChar=="-":
                    estado=13
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra=""
                    estado=0
                elif atualChar!="<":
                    atualChar=self.voltar(pos)
                    pos -= 1
                    palavra=atualChar
                    estado=12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra=""
                    estado=0

            if estado==15:
                palavra+=atualChar
                if atualChar==">":
                    estado=12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra=""
                    estado=0
                elif atualChar != "=":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    palavra = atualChar
                    estado = 12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
            if estado==16:
                palavra+=atualChar
                estado=17
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                palavra = ""
                estado = 0

            if estado==18:
                palavra+=atualChar
                estado=12
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                estado=0
                palavra=""

            if estado==19:
                palavra += atualChar
                estado = 8
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                estado = 0
                palavra = ""
            if estado==20:
                if self.ehCharMin(atualChar) or self.ehCharMax(atualChar) or self.ehNumero(atualChar) or atualChar == "_":
                    estado = 20
                    palavra += atualChar
                else:
                    if self.palavrasReservadas(palavra):
                        estado=10
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                    else:
                        estado = 22
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
            if self.ehEOF(pos):
                return None
            else:
                atualChar = self.proxChar(pos)
                pos += 1

            # print(palavra+"\n")

    def ehNumero(self, char):
        if "0" <= char <= "9":
            return True
        return False

    def ehCharMin(self, char):
        if (char >= "a" and char <= "z"):
            return True
        return False
    def ehCharMax(self, char):
        if (char >= "A" and char <= "Z"):
            return True
        return False

    def ehOperador(self, char):
        if char == ">" or char == "<" or char == "=" or char == "!":
            return True
        return False

    def ehEspaco(self, char):
        if char == " " or char == "\t" or char == "\n" or char == "\r" or char == "\f":
            return True
        return False

    def ehString(self, char):
        if char == '"':
            return True
        return False

    def alertaComentarioMenos(self,char):
        if char=="-":
            return True
        return False
    """
        def alertaComentarioMult(self,char):
        if char=="(":
            return True
        return False
    """

    def palavrasReservadas(self,palavra):
        lista=["class","else","false","fi","if","in","inherits","isvoid","let","loop","pool","then","while","case",
               "esac", "new", "of","not","true","self", "SELF_TYPE"]
        if palavra in lista:
            return True
        return False

    def ehOperadorRel(self,char):
        lista=["<","=","~"]
        if char in lista:
            return True
        return False

    def ehDelimitador(self,char):
        lista=[";",":",",","@","."]
        if char in lista:
            return True
        return False

    def ehDelimitadorEspe(self,char):
        lista = ['(',')', '[',']','{','}']
        if char in lista:
            return True
        return False

    def ehOperadorArit(self,char):
        lista = ['+','*', '/']
        if char in lista:
            return True
        return False

    def proxChar(self, pos):
        return self.conteudo[pos + 1]

    def voltar(self, pos):
        return self.conteudo[pos - 1]

    def ehEOF(self, pos):
        return pos == (len(self.conteudo)) - 1
