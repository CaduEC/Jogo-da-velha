import random

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'O'
        self.jogador_maquina = 'X'

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogador_atual, self.jogador_maquina = self.jogador_maquina, self.jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    def verificar_vitoria(self, jogador):
        # Verificar linhas e colunas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == jogador:
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == jogador:
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento == ' ':
                    return False
        return True

class JogoDaVelhaVsMaquina(JogoDaVelha):
    def __init__(self):
        super().__init__()

    def fazer_jogada_maquina(self):
        while True:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if self.tabuleiro[linha][coluna] == ' ':
                self.tabuleiro[linha][coluna] = 'Y'  # Máquina usa 'Y' como marcação
                self.jogador_atual, self.jogador_maquina = self.jogador_maquina, self.jogador_atual
                break

    def jogar(self):
        while not self.verificar_vitoria(self.jogador_atual) and not self.verificar_empate():
            self.imprimir_tabuleiro()

            if self.jogador_atual == 'O':
                linha = int(input("Digite a linha da sua jogada (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna da sua jogada (0, 1 ou 2): "))
                self.fazer_jogada(linha, coluna)
            else:
                print("Vez da máquina:")
                self.fazer_jogada_maquina()

        self.imprimir_tabuleiro()

        if self.verificar_vitoria('O'):
            print("Você venceu!")
        elif self.verificar_vitoria('Y'):  # Verifica se a máquina venceu com 'Y'
            print("A máquina venceu!")
        else:
            print("O jogo empatou.")

# Exemplo de uso
jogo_vs_maquina = JogoDaVelhaVsMaquina()
jogo_vs_maquina.jogar()
