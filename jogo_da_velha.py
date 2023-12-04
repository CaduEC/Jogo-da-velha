class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    def verificar_vitoria(self):
        # Verificar linhas e colunas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento == ' ':
                    return False
        return True

class JogoDaVelhaModificado(JogoDaVelha):
    def __init__(self):
        super().__init__()

    def fazer_jogada(self, linha, coluna):
        super().fazer_jogada(linha, coluna)
        if self.verificar_vitoria():
            print(f"Jogador {self.jogador_atual} venceu!")
        elif self.verificar_empate():
            print("O jogo empatou.")
        else:
            self.imprimir_tabuleiro()


# Exemplo de uso
jogo = JogoDaVelhaModificado()

while not jogo.verificar_vitoria() and not jogo.verificar_empate():
    jogo.imprimir_tabuleiro()
    linha = int(input("Digite a linha da sua jogada (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna da sua jogada (0, 1 ou 2): "))
    jogo.fazer_jogada(linha, coluna)
