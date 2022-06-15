import tokenCool
from tokenCool import TokenCool


class AnalisadorLexico(TokenCool):
    # inicializando o construtor do analisador
    def __init__(self, conteudo):
        # Herança do Token Cool
        super().__init__()
        # Conteúudo do arquivo
        self.conteudo = conteudo
        # Estado inicial do automato
        self.estado = 0
        # Inicializando o Token Cool
        self.tokenC = TokenCool()

    # Contrói o Token até terminar o programa.
    def proxToken(self):
        # Caractere atual.
        atualChar = self.conteudo[0]
        # Armazena palavra.
        palavra = ""
        # Estado.
        estado = 0
        # Inicialanzo loop.
        loop = True
        # Posição do vetor do caractere atual.
        pos = 0
        # Sinalizador do começo de uma String.
        contString = 0
        # Sinalizador do começo de um comentário --....
        contComent = 0
        # Sinalizador do começo de um comentário (*...*)..
        contComentMult = 0
        # Quantidade de delimitadores.
        contDeli = 0
        # Posição do token no programa.
        posLinha = 1

        while (loop == True):
            # Verifica o estado inicial e vai para o próximo estado.
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
                    estado = 7
                elif self.alertaComentarioMult(atualChar):
                    estado = 21

                elif self.ehOperadorRel(atualChar):
                    if atualChar == "<":
                        estado = 11
                    elif atualChar == "~":
                        estado = 18
                    else:
                        estado = 15

                elif self.ehOperadorArit(atualChar):
                    estado = 19

                elif self.ehDelimitador(atualChar) or self.ehDelimitadorEspe(atualChar):
                    estado = 16
                elif self.ehCharMax(atualChar):
                    estado = 20
                elif self.ehInvalido(atualChar):
                    estado = 22
            # Estado que verificar se a token identificador ou palavra reservada
            if estado == 1:
                if self.ehCharMin(atualChar) or self.ehCharMax(atualChar) or self.ehNumero(
                        atualChar) or atualChar == "_":
                    estado = 1
                    palavra += atualChar

                else:
                    if self.palavrasReservadas(palavra):
                        estado = 10
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                        atualChar = self.voltar(pos)
                        pos -= 1
                    else:
                        # Condição de identificador
                        estado = 2
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                        atualChar = self.voltar(pos)
                        pos -= 1
            # Estado que verifica se o token é um número.
            if estado == 3:
                if self.ehNumero(atualChar):
                    estado = 3
                    palavra += atualChar
                else:
                    # Condições que encerram o número
                    if self.ehOperadorArit(atualChar) or self.ehEspaco(atualChar) or self.ehOperadorRel(
                            atualChar) or self.ehDelimitador(atualChar) or self.ehDelimitadorEspe(atualChar):
                        if atualChar not in ["@", "."]:
                            estado = 4
                            TokenCool.mostrarToken(self.tokenC, estado, palavra)
                            estado = 0
                            palavra = ""
                            atualChar = self.voltar(pos)
                            pos -= 1
                        else:
                            print("Posicao do erro na linha:", posLinha)
                            raise Exception('Numero desconhecido')
                    else:
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Numero desconhecido')

            # Verifica se o token é uma String
            if estado == 5:
                # Particularidades do Cool. Contra barra em string.
                if atualChar == "\\":
                    palavra = palavra
                else:
                    palavra += atualChar
                # Verifica se tem null na String
                if atualChar == "0":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    if atualChar == "\\":
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Null em string')
                    atualChar = self.proxChar(pos)
                    pos += 1
                # Verifica quebra de linha em String.
                if atualChar == "\n":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    if atualChar != '\\':
                        print("Posicao do erro na linha:", posLinha)
                        raise Exception('Quebra de linha')
                    atualChar = self.proxChar(pos)
                    pos += 1
                # Verifica se é uma String normal.
                if atualChar == '"' and contString == 1:
                    estado = 6
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado = 0
                    palavra = ""
                    contString = 0
                else:
                    contString = 1
            # Estado do comentário do --...--.
            if estado == 7:
                if atualChar == "-":
                    contComent += 1
                if contComent == 1 and not atualChar == "-":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    palavra += atualChar
                    estado = 8
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
                    contComent = 0
                if atualChar=="\n" and contComent>=2:
                    estado=0
                    palavra=""


            # Estado em que os operadores relacionais são iniciados em <.
            if estado == 11:
                palavra += atualChar
                # Condição se for <=.
                if atualChar == "=":
                    estado = 12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
                # Condição se for <-(Atribuição).
                elif atualChar == "-":
                    estado = 13
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
                # Condição se for <.
                elif atualChar != "<":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    palavra = atualChar
                    estado = 12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
            # Estado que verifica se o operador é iniciado com =.
            if estado == 15:
                palavra += atualChar
                # Condição se o operador for =>
                if atualChar == ">":
                    estado = 12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
                # Condição se o operador for só o =.
                elif atualChar != "=":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    palavra = atualChar
                    estado = 12
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    palavra = ""
                    estado = 0
            # Estado que verifica se os tokens são delimitadores.
            if estado == 16:
                if self.ehDelimitadorEspe(atualChar):
                    contDeli += 1
                palavra += atualChar
                estado = 17
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                palavra = ""
                estado = 0
            # Estado que verifica se o token é ~.
            if estado == 18:
                palavra += atualChar
                estado = 12
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                estado = 0
                palavra = ""
            # Estado que verifica se o token é operador aritmético.
            if estado == 19:
                palavra += atualChar
                estado = 8
                TokenCool.mostrarToken(self.tokenC, estado, palavra)
                estado = 0
                palavra = ""
            # Estado que verifica se o token é tipo(type).
            if estado == 20:
                if self.ehCharMin(atualChar) or self.ehCharMax(atualChar) or self.ehNumero(
                        atualChar) or atualChar == "_":
                    estado = 20
                    palavra += atualChar
                else:
                    if self.palavrasReservadas(palavra):
                        estado = 10
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                    else:
                        estado = 22
                        TokenCool.mostrarToken(self.tokenC, estado, palavra)
                        estado = 0
                        palavra = ""
                        atualChar = self.voltar(pos)
                        pos -= 1
            # Estado que verifica se é um comentário com (*..*)
            if estado == 21:
                if contComentMult == 0 and atualChar == "*":
                    contComentMult += 1
                elif contComentMult == 0 and self.proxChar(pos) != "*":
                    estado = 17
                    palavra += atualChar
                    contDeli += 1
                    TokenCool.mostrarToken(self.tokenC, estado, palavra)
                    estado = 0
                    palavra = ""

                if estado == 21 and atualChar == ")":
                    atualChar = self.voltar(pos)
                    pos -= 1
                    if atualChar == "*":
                        atualChar = self.proxChar(pos)
                        estado = 0
                        contComentMult = 0
                    atualChar = self.proxChar(pos)
                    pos += 1
            # Estado que verifica se o caractere é inválido.
            if estado == 22:
                print("Posicao do erro na linha:", posLinha)
                raise Exception('letra desconhecida')
            # Condição que verifica se o arquivo terminou.
            if self.ehEOF(pos):
                if contComent == 2 or contComentMult == 1:
                    raise Exception('Comentário nao fechado')
                elif contString == 1:
                    raise Exception('String nao fechada')
                elif contDeli % 2 != 0:
                    print(contDeli)
                    raise Exception('Delimitador nao fechado')
                return None
            # Condição para o próximo caractere.
            else:
                atualChar = self.proxChar(pos)
                pos += 1
                if atualChar == "\n":
                    posLinha += 1

    # Verifica se é um número de 0 a 9.
    def ehNumero(self, char):
        if "0" <= char <= "9":
            return True
        return False

    # Verifica se é um caractere de letra minúscula.
    def ehCharMin(self, char):
        if (char >= "a" and char <= "z"):
            return True
        return False

    # Verifica se é um caractere de letra maiúscula.
    def ehCharMax(self, char):
        if (char >= "A" and char <= "Z"):
            return True
        return False

    # Verifica se é espaço, tabulações e similares.
    def ehEspaco(self, char):
        if char == " " or char == "\t" or char == "\n" or char == "\r" or char == "\f" or char == "\v":
            return True
        return False

    # Verifica se é o começo de uma string
    def ehString(self, char):
        if char == '"':
            return True
        return False

    # Verifica se é o começo de um comentário com "-".
    def alertaComentarioMenos(self, char):
        if char == "-":
            return True
        return False

    # Verifica se é o começo de um comentário com "(".
    def alertaComentarioMult(self, char):
        if char == "(":
            return True
        return False

    # Verifica se uma palavra é reservada.
    def palavrasReservadas(self, palavra):
        lista = ["class", "else", "false", "fi", "if", "in", "inherits", "isvoid", "let", "loop", "pool", "then",
                 "while", "case",
                 "esac", "new", "of", "not", "true", "self", "SELF_TYPE"]
        if palavra in lista:
            return True
        return False

    # Verifica se é um operador relacional.
    def ehOperadorRel(self, char):
        lista = ["<", "=", "~"]
        if char in lista:
            return True
        return False

    # Verifica se é um delimitador.
    def ehDelimitador(self, char):
        lista = [";", ":", ",", "@", "."]
        if char in lista:
            return True
        return False

    # Verifica se é um delimitador especial.
    def ehDelimitadorEspe(self, char):
        lista = ['(', ')', '[', ']', '{', '}']
        if char in lista:
            return True
        return False

    # Verifica se é um operador aritmético.
    def ehOperadorArit(self, char):
        lista = ['+', '*', '/', "-"]
        if char in lista:
            return True
        return False

    # Verifica se é um caractere inválido.
    def ehInvalido(self, char):
        lista = ['$', "#", "null", "!", "%", "&", "'", "?", "^", "`", "|"]
        if char in lista:
            return True
        return False

    # Avança na lista para o próximo caractere.
    def proxChar(self, pos):
        return self.conteudo[pos + 1]

    # Volta na lista para o caractere anterior.
    def voltar(self, pos):
        return self.conteudo[pos - 1]

    # Verifica se é o final do programa.
    def ehEOF(self, pos):
        return pos == (len(self.conteudo)) - 1