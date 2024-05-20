import random

class JogoDaVelha:
    def __init__(self):
        self.__tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.__jogador_atual = 'O'
        self.__jogador_maquina = 'X'

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @property
    def jogador_atual(self):
        return self.__jogador_atual

    def __alternar_jogador(self):
        self.__jogador_atual = 'X' if self.__jogador_atual == 'O' else 'O'

    def imprimir_tabuleiro(self):
        for linha in self.__tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def fazer_jogada(self, linha, coluna):
        if self.__tabuleiro[linha][coluna] == ' ':
            self.__tabuleiro[linha][coluna] = self.__jogador_atual
            self.__alternar_jogador()
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    def verificar_vitoria(self, jogador):
        # Verificar linhas e colunas
        for i in range(3):
            if self.__tabuleiro[i][0] == self.__tabuleiro[i][1] == self.__tabuleiro[i][2] == jogador:
                return True
            if self.__tabuleiro[0][i] == self.__tabuleiro[1][i] == self.__tabuleiro[2][i] == jogador:
                return True

        # Verificar diagonais
        if self.__tabuleiro[0][0] == self.__tabuleiro[1][1] == self.__tabuleiro[2][2] == jogador:
            return True
        if self.__tabuleiro[0][2] == self.__tabuleiro[1][1] == self.__tabuleiro[2][0] == jogador:
            return True

        return False

    def verificar_empate(self):
        for linha in self.__tabuleiro:
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
                self.tabuleiro[linha][coluna] = 'X'  # Máquina usa 'X' como marcação
                self._JogoDaVelha__alternar_jogador()
                break

    def jogar(self):
        while True:  # Loop externo para permitir jogar novamente
            while not self.verificar_vitoria('O') and not self.verificar_vitoria('X') and not self.verificar_empate():
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
                print("Parabéns! Você venceu!")
            elif self.verificar_vitoria('X'):
                print("Você perdeu. Melhor sorte da próxima vez!")
            else:
                print("O jogo terminou em empate.")

            # Pergunta se deseja jogar novamente
            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() != 's':
                break  # Sai do loop externo se não desejar jogar novamente

            # Reinicializa o tabuleiro para uma nova partida
            self._JogoDaVelha__tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
            self._JogoDaVelha__jogador_atual = 'O'

# Exemplo de uso
jogo_vs_maquina = JogoDaVelhaVsMaquina()
jogo_vs_maquina.jogar()
