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
        while True:
            while not self.verificar_vitoria(self.jogador_atual) and not self.verificar_vitoria('Y') and not self.verificar_empate():
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
            elif self.verificar_vitoria('Y'):
                print("A máquina venceu!")
            else:
                print("O jogo empatou.")

            # Pergunta se o jogador quer jogar novamente
            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
            if jogar_novamente != 's':
                print("Obrigado por jogar. Até a próxima!")
                break
            else:
                # Reinicia o jogo
                self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
                self.jogador_atual, self.jogador_maquina = 'O', 'X'

# Exemplo de uso
jogo_vs_maquina = JogoDaVelhaVsMaquina()
jogo_vs_maquina.jogar()
