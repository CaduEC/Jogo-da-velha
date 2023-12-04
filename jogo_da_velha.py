class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]

    def exibir_tabuleiro(self):
        print()
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-------")
            print(self.tabuleiro[i], end=' ')
        print()

    def jogar(self, posicao, jogador):
        if self.tabuleiro[posicao] == ' ':
            self.tabuleiro[posicao] = jogador
        else:
            print("Essa posição já está ocupada.")

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_atual = 'X'

    def alternar_jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def verificar_vencedor(self):
        linhas = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]

        for linha in linhas:
            if self.tabuleiro.tabuleiro[linha[0]] == self.tabuleiro.tabuleiro[linha[1]] == self.tabuleiro.tabuleiro[linha[2]] != ' ':
                return self.tabuleiro.tabuleiro[linha[0]]

        return None

    def main(self):
        self.tabuleiro.exibir_tabuleiro()
        for i in range(9):
            while True:
                posicao = int(input(f"{self.jogador_atual}, digite a posição onde deseja jogar (0-8): "))
                self.tabuleiro.jogar(posicao, self.jogador_atual)
                self.tabuleiro.exibir_tabuleiro()
                vencedor = self.verificar_vencedor()
                if vencedor:
                    print(f"O vencedor é o {vencedor}!")
                    break
                elif i == 8:
                    print("Deu velha!")
                    break
                else:
                    self.alternar_jogador()

jogo = Jogo()
jogo.main()
