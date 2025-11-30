import tkinter as tk

# cores da tela:
cor_titulo = "#FF4438"
cor_fundo = "#091A23"
cor_botao = "#351D22"
cor_botao_hover = "#8A221C"
cor_text_botao = "white"

# função para estilizar botão
def estilizar(botao):
    botao.config(bg=cor_botao, fg=cor_text_botao, activebackground=cor_botao_hover, activeforeground=cor_text_botao,relief="flat", bd=0, font=("Arial", 11, "bold"), cursor="hand2")
    botao.bind("<Enter>", lambda e: botao.config(bg=cor_botao_hover))
    botao.bind("<Leave>", lambda e: botao.config(bg=cor_botao))

janela = tk.Tk()
janela.title("Sistema de notas rápidas")
janela.geometry("400x350")
janela.resizable(False, False)

tela_inicial = tk.Frame(janela, bg=cor_fundo)
tela_inicial.pack(fill="both", expand=True)

titulo = tk.Label( tela_inicial, text="SISTEMA DE NOTAS RÁPIDAS", font=("Arial",16,"bold"), bg=cor_fundo, fg=cor_titulo)
titulo.pack(pady=20)

btn_adicionar = tk.Button(tela_inicial, text="ADICIONAR NOTAS", width=20, height=2)
estilizar(btn_adicionar)
btn_adicionar.pack(pady=5)

btn_listar = tk.Button(tela_inicial, text="LISTAR NOTAS", width=20, height=2)
estilizar(btn_listar)
btn_listar.pack(pady=5)

btn_remover = tk.Button(tela_inicial, text="REMOVER NOTAS", width=20, height=2)
estilizar(btn_remover)
btn_remover.pack(pady=5)

btn_atualizar = tk.Button(tela_inicial, text="ATUALIZAR NOTA", width=20, height=2)
estilizar(btn_atualizar)
btn_atualizar.pack(pady=5)

icone_voltar = tk.PhotoImage()
btn_voltar = tk.Button(tela_inicial, text="←", width=3, height=1)
estilizar(btn_voltar)
btn_voltar.place(x=10, y=310)

janela.mainloop()
