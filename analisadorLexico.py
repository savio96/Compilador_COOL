import tokenCool
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
        # print(len(self.conteudo))

        while (loop == True):
            if estado == 0:
                if self.ehChar(atualChar):
                    estado = 1

                elif self.ehNumero(atualChar):
                    estado = 3

                elif self.ehEspaco(atualChar):
                    estado = 0

                elif self.ehString(atualChar):
                    estado = 5

            if estado == 1:
                if self.ehChar(atualChar) or self.ehNumero(atualChar) or atualChar == "_":
                    estado = 1
                    palavra += atualChar
                    # atualChar = self.proxChar(pos)
                    # pos+=1

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

                palavra+=atualChar

                if atualChar=='"' and contString==1:
                    estado=6
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado=0
                    palavra=""
                    contString=0
                else:
                    contString = 1
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

    def ehChar(self, char):
        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
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

    def proxChar(self, pos):
        return self.conteudo[pos + 1]

    def voltar(self, pos):
        return self.conteudo[pos - 1]

    def ehEOF(self, pos):
        return pos == (len(self.conteudo)) - 1
