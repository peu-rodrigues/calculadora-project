import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox, Toplevel
import math
import time

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Profissional")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Tema automático
        hora = time.localtime().tm_hour
        if 6 <= hora < 18:
            self.style = Style(theme='cosmo')
        else:
            self.style = Style(theme='superhero')

        self.expr = ""
        self.historico = []

        self.display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT)
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)

        # Frame para botões
        botoes_frame = tk.Frame(root)
        botoes_frame.pack()

        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '(', ')', '√']
        ]

        cientificos = [
            ['sin', 'cos', 'tan', '^'],
            ['log', 'ln', 'pi', 'e']
        ]

        # Adicionar botões numéricos
        for i, linha in enumerate(botoes):
            for j, btn in enumerate(linha):
                self.criar_botao(botoes_frame, btn, i, j)

        # Adicionar botões científicos
        for i, linha in enumerate(cientificos):
            for j, btn in enumerate(linha):
                self.criar_botao(botoes_frame, btn, i+5, j)

        # Botão para ver histórico
        hist_btn = tk.Button(root, text="Ver Histórico", font=("Arial", 14), command=self.mostrar_historico)
        hist_btn.pack(pady=10)

        # Bind do teclado físico
        self.root.bind("<Key>", self.teclado)

    def criar_botao(self, frame, texto, linha, coluna):
        botao = tk.Button(
            frame, text=texto, font=("Arial", 18), relief=tk.GROOVE, bd=2,
            bg="#1f6aa5", fg="white", activebackground="#144e75",
            activeforeground="white", command=lambda b=texto: self.clique(b),
            width=5, height=2
        )
        botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

    def clique(self, botao):
        if botao == 'C':
            self.expr = ""
            self.atualiza_display()
        elif botao == '=':
            self.calcular()
        else:
            self.expr += botao
            self.atualiza_display()

    def calcular(self):
        try:
            expr_mod = self.expr.replace('√', 'math.sqrt').replace('^', '**')
            expr_mod = expr_mod.replace('sin', 'math.sin')
            expr_mod = expr_mod.replace('cos', 'math.cos')
            expr_mod = expr_mod.replace('tan', 'math.tan')
            expr_mod = expr_mod.replace('log', 'math.log10')
            expr_mod = expr_mod.replace('ln', 'math.log')
            expr_mod = expr_mod.replace('pi', str(math.pi))
            expr_mod = expr_mod.replace('e', str(math.e))

            resultado = str(eval(expr_mod))
            self.historico.append(f"{self.expr} = {resultado}")
            self.expr = resultado
            self.atualiza_display()
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida")
            self.expr = ""
            self.atualiza_display()

    def atualiza_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expr)

    def mostrar_historico(self):
        hist_window = Toplevel(self.root)
        hist_window.title("Histórico")
        hist_window.geometry("300x200")

        hist_text = tk.Text(hist_window, state='normal', font=("Arial", 12))
        hist_text.pack(fill="both", expand=True, padx=10, pady=10)

        for item in self.historico[-10:]:
            hist_text.insert(tk.END, item + "\n")

        hist_text.config(state='disabled')

    def teclado(self, event):
        tecla = event.keysym

        if tecla in '0123456789':
            self.expr += tecla
        elif tecla in ['plus', 'KP_Add']:
            self.expr += '+'
        elif tecla in ['minus', 'KP_Subtract']:
            self.expr += '-'
        elif tecla in ['asterisk', 'KP_Multiply']:
            self.expr += '*'
        elif tecla in ['slash', 'KP_Divide']:
            self.expr += '/'
        elif tecla == 'period':
            self.expr += '.'
        elif tecla == 'parenleft':
            self.expr += '('
        elif tecla == 'parenright':
            self.expr += ')'
        elif tecla == 'Return':
            self.calcular()
        elif tecla == 'BackSpace':
            self.expr = self.expr[:-1]
        elif tecla == 'Escape':
            self.expr = ""
        elif tecla == 's':
            self.expr += 'sin'
        elif tecla == 'c':
            self.expr += 'cos'
        elif tecla == 't':
            self.expr += 'tan'
        elif tecla == 'l':
            self.expr += 'log'
        elif tecla == 'n':
            self.expr += 'ln'
        elif tecla == 'r':
            self.expr += '√'
        elif tecla == 'p':
            self.expr += 'pi'
        elif tecla == 'e':
            self.expr += 'e'
        elif tecla == 'asciicircum':
            self.expr += '^'

        self.atualiza_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
