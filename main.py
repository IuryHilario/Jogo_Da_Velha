from tkinter import *
from tkinter import messagebox
from random import randint


class Jogo_Da_Velha_Script(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.geometry('+650+200')

        self.Jogo()

    def Jogo(self):

        self.Imagem_X = PhotoImage(file='Letra_X.png')
        self.Imagem_O = PhotoImage(file='Letra_O.png')

        self.Velha = 0

        self['bg'] = 'black'
        self.title('Jogo Da Velha')

        self.Vez_Do_Jogador = Label(self, font=('Comic Sans MS', 20), bg='#6fb7d2', bd=5, relief=RAISED)
        self.Vez_Do_Jogador.grid(row=0, column=0, columnspan=5, sticky='NEWS')

        for L in range(1, 4):
            for C in range(1, 4):
                self.Local = Button(self, width=20, height=10, relief=FLAT, command=lambda L=L, C=C: self.Jogadas(L, C))
                self.Local.grid(row=L, column=C, sticky='NEWS', padx=5, pady=5)

        self.V = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        Jogador_1 = randint(1, 2)

        if Jogador_1 == 1:
            self.Vez_Do_Jogador['text'] = 'Vez Do X'
            self.Qual_Jogador_Agora = 0

        if Jogador_1 == 2:
            self.Vez_Do_Jogador['text'] = 'Vez Do O'
            self.Qual_Jogador_Agora = 1

    def Jogadas(self, Linha, Coluna):
        self.Velha += 1

        Linha -= 1
        Coluna -= 1

        self.Jogador_X = 1
        self.Jogador_Y = -1

        if self.Qual_Jogador_Agora == 0:

            self.Vez_Do_Jogador['text'] = 'Vez Do O'
            self.Qual_Jogador_Agora += 1

            self.V[Linha][Coluna] = self.Jogador_X

            self.Local = Label(self, width=20, height=10, relief=FLAT, image=self.Imagem_X)
            self.Local.grid(row=Linha + 1, column=Coluna + 1, sticky='NEWS', padx=5, pady=5)

            if self.Velha == 9:
                self.Vez_Do_Jogador['text'] = 'Velha!'


        elif self.Qual_Jogador_Agora == 1:

            self.Vez_Do_Jogador['text'] = 'Vez Do X'
            self.Qual_Jogador_Agora = 0

            self.V[Linha][Coluna] = self.Jogador_Y

            self.Local = Label(self, width=20, height=10, relief=FLAT, image=self.Imagem_O)
            self.Local.grid(row=Linha + 1, column=Coluna + 1, sticky='NEWS', padx=5, pady=5)

            if self.Velha == 9:
                self.Vez_Do_Jogador['text'] = 'Velha!'

        self.Ganhador(Linha, Coluna)

    def Ganhador(self, L, C):
        Linha = self.V

        Coluna = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        Vertical = [[Linha[0][0], Linha[1][1], Linha[2][2]], [Linha[0][2], Linha[1][1], Linha[2][0]]]

        String_1 = - 1
        String_2 = - 1

        for Horizonte in Linha:
            String_2 += 1

            for Reto in Horizonte:
                String_1 += 1

                Coluna[String_1][String_2] = Reto

                if String_1 == 2:
                    String_1 = - 1

        if sum(Linha[L]) == 3 or sum(Coluna[C]) == 3 or sum(Vertical[0]) == 3 or sum(Vertical[1]) == 3:
            self.Vez_Do_Jogador['text'] = 'Vencedor é o "X"'
            CX = messagebox.askquestion('Jogo Da Velha', 'Jogador "X" Venceu\n     Continuar?')
            self.Velha -= 1
            if CX == 'yes':
                self.Reiniciar()

            if CX == 'no':
                self.Fim()

        if sum(Linha[L]) == -3 or sum(Coluna[C]) == -3 or sum(Vertical[0]) == -3 or sum(Vertical[1]) == -3:
            self.Vez_Do_Jogador['text'] = 'Vencedor é o "O"'
            CY = messagebox.askquestion('Jogo Da Velha', 'Jogador "O" Venceu\n     Continuar?')
            self.Velha -= 1

            if CY == 'yes':
                self.Reiniciar()

            if CY == 'no':
                self.Fim()

        if self.Velha == 9:
            C = messagebox.askquestion('Jogo Da Velha', 'Não Houve Ganhador, Deu Velha!!\n\tContinuar?')

            if C == 'yes':
                self.Reiniciar()

            if C == 'no':
                self.Fim()

    def Reiniciar(self):
        try:
            self.destroy()
        except:
            pass

        self.__init__()

    def Fim(self):
        self.quit()


if __name__ == '__main__':
    Jogo_Da_Velha_Script().mainloop()
