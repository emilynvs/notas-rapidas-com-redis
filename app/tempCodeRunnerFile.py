import tkinter as tk
from notas_service import adicionar_nota, listar_tudo, remover_nota, atualizar_nota


# cores da tela:
cor_titulo = "#FF4438"
cor_fundo = "#091A23"
cor_botao = "#351D22"
cor_botao_hover = "#8A221C"
cor_text_botao = "white"


# função para estilizar botão
def estilizar(botao):
    botao.config(
        bg=cor_botao,
        fg=cor_text_botao,
        activebackground=cor_botao_hover,
        activeforeground=cor_text_botao,
        relief="flat",
        bd=0,
        font=("Arial", 11, "bold"),
        cursor="hand2"
    )
    botao.bind("<Enter>", lambda e: botao.config(bg=cor_botao_hover))
    botao.bind("<Leave>", lambda e: botao.config(bg=cor_botao))


# ================================================================
#   JANELAS PEQUENAS
# ================================================================

def janela_adicionar():
    win = tk.Toplevel(janela)
    win.title("Adicionar Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)
    win.resizable(False, False)

    tk.Label(win, text="Digite a nota:", bg=cor_fundo, fg="white", font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def salvar():
        texto = entrada.get()
        if texto.strip():
            adicionar_nota(texto)
            win.destroy()

    btn = tk.Button(win, text="Adicionar", width=15, height=1, command=salvar)
    estilizar(btn)
    btn.pack(pady=10)



def janela_listar():
    win = tk.Toplevel(janela)
    win.title("Listar Notas")
    win.geometry("300x250")
    win.config(bg=cor_fundo)
    win.resizable(False, False)

    tk.Label(win, text="Suas notas:", bg=cor_fundo, fg="white", font=("Arial", 12)).pack(pady=10)

    lista = tk.Listbox(win, width=32, height=8)
    lista.pack(pady=5)

    notas = listar_tudo()

    if not notas:
        lista.insert(tk.END, "Nenhuma nota encontrada.")
    else:
        for nota in notas:
            lista.insert(tk.END, nota)



def janela_remover():
    win = tk.Toplevel(janela)
    win.title("Remover Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)
    win.resizable(False, False)

    tk.Label(win, text="ID da nota para remover:", bg=cor_fundo, fg="white", font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def remover():
        id_nota = entrada.get()
        if id_nota.strip():
            remover_nota(id_nota)
            win.destroy()

    btn = tk.Button(win, text="Remover", width=15, command=remover)
    estilizar(btn)
    btn.pack(pady=10)



def janela_atualizar():
    win = tk.Toplevel(janela)
    win.title("Atualizar Nota")
    win.geometry("300x220")
    win.config(bg=cor_fundo)
    win.resizable(False, False)

    tk.Label(win, text="ID da nota:", bg=cor_fundo, fg="white", font=("Arial", 12)).pack(pady=10)
    entrada_id = tk.Entry(win, width=25, font=("Arial", 12))
    entrada_id.pack(pady=5)

    tk.Label(win, text="Novo valor:", bg=cor_fundo, fg="white", font=("Arial", 12)).pack(pady=10)
    entrada_novo = tk.Entry(win, width=25, font=("Arial", 12))
    entrada_novo.pack(pady=5)

    def atualizar():
        id_nota = entrada_id.get()
        novo_valor = entrada_novo.get()
        if id_nota.strip() and novo_valor.strip():
            atualizar_nota(id_nota, novo_valor)
            win.destroy()

    btn = tk.Button(win, text="Atualizar", width=15, command=atualizar)
    estilizar(btn)
    btn.pack(pady=10)



# ================================================================
#   TELA PRINCIPAL
# ================================================================
janela = tk.Tk()
janela.title("Sistema de notas rápidas")
janela.geometry("400x350")
janela.resizable(False, False)

tela_inicial = tk.Frame(janela, bg=cor_fundo)
tela_inicial.pack(fill="both", expand=True)

titulo = tk.Label(
    tela_inicial,
    text="SISTEMA DE NOTAS RÁPIDAS",
    font=("Arial", 16, "bold"),
    bg=cor_fundo,
    fg=cor_titulo
)
titulo.pack(pady=20)

btn_adicionar = tk.Button(tela_inicial, text="ADICIONAR NOTAS", width=20, height=2, command=janela_adicionar)
estilizar(btn_adicionar)
btn_adicionar.pack(pady=5)

btn_listar = tk.Button(tela_inicial, text="LISTAR NOTAS", width=20, height=2, command=janela_listar)
estilizar(btn_listar)
btn_listar.pack(pady=5)

btn_remover = tk.Button(tela_inicial, text="REMOVER NOTAS", width=20, height=2, command=janela_remover)
estilizar(btn_remover)
btn_remover.pack(pady=5)

btn_atualizar = tk.Button(tela_inicial, text="ATUALIZAR NOTA", width=20, height=2, command=janela_atualizar)
estilizar(btn_atualizar)
btn_atualizar.pack(pady=5)

btn_voltar = tk.Button(tela_inicial, text="←", width=3, height=1)
estilizar(btn_voltar)
btn_voltar.place(x=10, y=310)

janela.mainloop()
