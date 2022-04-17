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
        contDeli=0
        posLinha=1
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
                elif self.alertaComentarioMult(atualChar):
                    estado=21

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
                elif self.ehInvalido(atualChar):
                    estado=22
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
                        atualChar = self.voltar(pos)
                        pos -= 1
                    else:
                        estado = 2
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                        atualChar=self.voltar(pos)
                        pos-=1
            if estado == 3:
                if self.ehNumero(atualChar):
                    estado = 3
                    palavra += atualChar
                else:
                    if self.ehOperadorArit(atualChar) or self.ehEspaco(atualChar) or self.ehOperadorRel(atualChar) or self.ehDelimitador(atualChar) or self.ehDelimitadorEspe(atualChar):
                        if atualChar not in ["@", "."]:
                            estado=4
                            TokenCool.mostrarToken(self.tokenC, estado, palavra)
                            estado=0
                            palavra=""
                            atualChar=self.voltar(pos)
                            pos-=1
                        else:
                            print("Posicao do erro na linha:", posLinha)
                            raise Exception('Numero desconhecido')
                    else:
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Numero desconhecido')
                    """
                    if self.ehOperadorArit(atualChar):
                        estado=4
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                        atualChar = self.voltar(pos)
                        pos -= 1
                elif self.ehEspaco(atualChar):
                    estado = 4
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado = 0
                    palavra = ""
                    atualChar = self.voltar(pos)
                    pos -= 1"""


            if estado == 5:
                if atualChar=="\\":
                    palavra=palavra
                else:
                    palavra+=atualChar
                if atualChar=="0":
                    atualChar=self.voltar(pos)
                    pos-=1
                    if atualChar=="\\":
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Null em string')
                    atualChar=self.proxChar(pos)
                    pos+=1
                if atualChar=="\n":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    if atualChar != '\\':
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Quebra de linha')
                    atualChar = self.proxChar(pos)
                    pos += 1
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
                    contComent = 0
                if contComent>=4:
                    estado=0
                    contComent=0
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
                if self.ehDelimitadorEspe(atualChar):
                    contDeli+=1
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
                        atualChar=self.voltar(pos)
                        pos-=1

            if estado==21:
                if contComentMult==0 and atualChar=="*":
                    contComentMult+=1
                elif contComentMult==0 and self.proxChar(pos)!="*":
                    estado=17
                    palavra+=atualChar
                    contDeli+=1
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado=0
                    palavra=""

                if estado==21 and atualChar==")":
                    atualChar=self.voltar(pos)
                    pos-=1
                    if atualChar=="*":
                        atualChar=self.proxChar(pos)
                        estado=0
                        contComentMult=0
                    atualChar = self.proxChar(pos)
                    pos+=1
            if estado==22:
                print("Posicao do erro na linha:", posLinha)
                raise Exception('letra desconhecida')

            if self.ehEOF(pos):
                if contComent==2 or contComentMult==1 :
                    raise Exception('Comentário nao fechado')
                elif contString==1:
                    raise Exception('String nao fechada')
                elif contDeli%2!=0:
                    print(contDeli)
                    raise Exception('Delimitador nao fechado')
                return None
            else:
                atualChar = self.proxChar(pos)
                pos += 1
                if atualChar=="\n":
                    posLinha+=1


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
    """
    def ehOperador(self, char):
        if char == ">" or char == "<" or char == "=" or char == "!":
            return True
        return False
    """
    def ehEspaco(self, char):
        if char == " " or char == "\t" or char == "\n" or char == "\r" or char == "\f" or char=="\v":
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

    def alertaComentarioMult(self,char):
        if char=="(":
            return True
        return False


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
        lista = ['+','*', '/',"-"]
        if char in lista:
            return True
        return False

    def ehInvalido(self,char):
        lista = ['$', "#","null","!","%","&","'","?","^","`","|"]
        if char in lista:
            return True
        return False

    def proxChar(self, pos):
        return self.conteudo[pos + 1]

    def voltar(self, pos):
        return self.conteudo[pos - 1]

    def ehEOF(self, pos):
        return pos == (len(self.conteudo)) - 1
