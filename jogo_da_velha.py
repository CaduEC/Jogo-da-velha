import random

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ']*3 for _ in range(3)]
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
            print("Posição já ocupada. Tente novamente.")

    def verificar_vitoria(self):
        # ... (código de verificação de vitória)

    def tabuleiro_cheio(self):
        return all(all(cell != ' ' for cell in row) for row in self.tabuleiro)

class JogoDaVelhaVsMaquina(JogoDaVelha):
    def __init__(self, jogador):
        super().__init__()
        self.jogador = jogador

    def fazer_jogada(self, linha, coluna):
        super().fazer_jogada(linha, coluna)
        if not self.verificar_vitoria() and not self.tabuleiro_cheio():
            self.jogada_maquina()

    def jogada_maquina(self):
        print("Vez da máquina (O):")
        linha, coluna = self.escolher_jogada_maquina()
        super().fazer_jogada(linha, coluna)

    def escolher_jogada_maquina(self):
        jogadas_disponiveis = [(i, j) for i in range(3) for j in range(3) if self.tabuleiro[i][j] == ' ']
        return random.choice(jogadas_disponiveis)

# Exemplo de Uso
jogador_nome = input("Digite o nome do Jogador: ")

jogo = JogoDaVelhaVsMaquina(jogador_nome)

while not jogo.verificar_vitoria() and not jogo.tabuleiro_cheio():
    jogo.imprimir_tabuleiro()

    if jogo.jogador_atual == 'X':
        try:
            linha = int(input("Digite a linha da sua jogada (0, 1, ou 2): "))
            coluna = int(input("Digite a coluna da sua jogada (0, 1, ou 2): "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            jogo.fazer_jogada(linha, coluna)
        else:
            print("Posição inválida. Tente novamente.")

    else:  # Vez da máquina
        jogo.jogada_maquina()

jogo.imprimir_tabuleiro()

if jogo.verificar_vitoria():
    print(f"Parabéns, {jogo.jogador}! Você venceu!")
else:
    print("Empate! O jogo terminou sem um vencedor.")
