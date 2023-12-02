import tkinter as tk
from tkinter import messagebox
import random

class JogoReciclagem:
    def __init__(self, root):
        self.root = root
        self.root.title("JOGO DA RECICLAGEM")

        self.perguntas = [
            {"pergunta": "Papel é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "papel.png", "resposta": "R"},
            {"pergunta": "Espelho é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "espelho_não.png", "resposta": "N"},
            {"pergunta": "Vidro é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "vidro.png", "resposta": "R"},
            {"pergunta": "Plástico é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "plástico.png", "resposta": "R"},
            {"pergunta": "Pilha é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "Pilha.png", "resposta": "N"},
            {"pergunta": "Metal é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "metal.PNG", "resposta": "R"},
            {"pergunta": "Jornal é reciclável (Responda R para Reciclável e N para Não Reciclável)?", "imagem": "jornal.png", "resposta": "R"},
            {"pergunta": "Esponja é reciclável (Responda R para Reciclável e N para Não Reciclável)?", "imagem": "esponja_não.PNG", "resposta": "N"},
            {"pergunta": "Lata é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "lata.png", "resposta": "R"},
            {"pergunta": "Solvente é reciclável? (Responda R para Reciclável e N para Não Reciclável)", "imagem": "solvente.PNG", "resposta": "N"}
        ]

        self.pontos = 0
        self.pergunta_atual = None

        self.criar_widgets()

    def criar_widgets(self):
        self.label_pergunta = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.label_pergunta.pack(pady=20)

        self.imagem_label = tk.Label(self.root)
        self.imagem_label.pack()

        self.resposta_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.resposta_entry.pack(pady=10)

        self.botao_responder = tk.Button(self.root, text="Responder", command=self.verificar_resposta)
        self.botao_responder.pack()

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if self.perguntas:
            self.pergunta_atual = random.choice(self.perguntas)
            self.label_pergunta.config(text=self.pergunta_atual["pergunta"])
            imagem = tk.PhotoImage(file=self.pergunta_atual["imagem"])
            self.imagem_label.config(image=imagem)
            self.imagem_label.image = imagem
        else:
            self.mostrar_resultado()

    def verificar_resposta(self):
        resposta_jogador = self.resposta_entry.get().upper()
        resposta_correta = self.pergunta_atual["resposta"]

        if resposta_jogador == resposta_correta:
            messagebox.showinfo("Resposta Correta", "Resposta correta!")
            self.pontos += 1
        else:
            messagebox.showinfo("Resposta Incorreta", "Resposta incorreta.")

        self.perguntas.remove(self.pergunta_atual)
        self.proxima_pergunta()

    def mostrar_resultado(self):
        mensagem = f"FIM DE JOGO\nVocê acertou {self.pontos} pergunta(s) de um total de 10."

        if self.pontos >= 8:
            mensagem += "\nPARABÉNS! Você está ajudando a preservar o meio ambiente."
        elif 4 <= self.pontos <= 7:
            mensagem += "\nVocê está no caminho certo, então vamos aprender mais para ajudar o meio ambiente."
        else:
            mensagem += "\nInfelizmente você não foi bem em suas respostas. Você deverá estudar mais em como preservar o meio ambiente."

        messagebox.showinfo("Resultado", mensagem)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoReciclagem(root)
    root.mainloop()

