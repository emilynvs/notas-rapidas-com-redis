import tkinter as tk
import notas_service as service
from tkinter import messagebox

# ---------- CORES ----------
cor_titulo = "#FF4438"
cor_fundo = "#091A23"
cor_botao = "#351D22"
cor_botao_hover = "#8A221C"
cor_text_botao = "white"

def janela_detalhes(nota):
    id_nota, texto, criado, atualizado = nota

    win = tk.Toplevel(janela)
    win.title("Detalhes da Nota")
    win.geometry("400x250")
    win.config(bg=cor_fundo)

    tk.Label(win, text=f"ID: {id_nota}", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=5)

    tk.Label(win, text=f"Texto: {texto}", bg=cor_fundo, fg="white",
             font=("Arial", 12), wraplength=350).pack(pady=5)

    tk.Label(win, text=f"Criado em: {criado}", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=5)

    tk.Label(win, text=f"Atualizado em: {atualizado}", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=5)



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



def janela_adicionar():
    win = tk.Toplevel(janela)
    win.title("Adicionar Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)

    tk.Label(win, text="Digite a nota:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def salvar():
        texto = entrada.get().strip()
        if texto:
            service.adicionar_nota(texto)
            win.destroy()

    btn = tk.Button(win, text="Adicionar", width=15, height=1, command=salvar)
    estilizar(btn)
    btn.pack(pady=10)


def janela_listar():
    win = tk.Toplevel(janela)
    win.title("Listar Notas")
    win.geometry("330x300")
    win.config(bg=cor_fundo)

    tk.Label(win, text="Suas notas:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)

    lista = tk.Listbox(win, width=40, height=12)
    lista.pack(pady=5)

    notas = service.listar_tudo()
    favoritas = service.listar_favoritas()

    fav_ids = {f[0] for f in favoritas}

    if not notas:
        lista.insert(tk.END, "Nenhuma nota encontrada.")
    else:
        for id_nota, texto, criado, atualizado in notas:
            estrela = "★ " if id_nota in fav_ids else ""
            lista.insert(
                tk.END,
                f"{estrela}{id_nota} | {texto} | Criado: {criado} | Atualizado: {atualizado}"
            )

    def abrir_detalhes(event):
        idx = lista.curselection()
        if not idx:
            return
        janela_detalhes(notas[idx[0]])

    lista.bind("<Double-Button-1>", abrir_detalhes)

def janela_remover():
    win = tk.Toplevel(janela)
    win.title("Remover Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)

    tk.Label(win, text="ID da nota:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def remover():
        _id = entrada.get().strip()
        if service.remover_nota(_id):
            win.destroy()
        else:
            messagebox.showerror("Erro", "ID não encontrado.")


    btn = tk.Button(win, text="Remover", width=15, command=remover)
    estilizar(btn)
    btn.pack(pady=10)


def janela_atualizar():
    win = tk.Toplevel(janela)
    win.title("Atualizar Nota")
    win.geometry("300x220")
    win.config(bg=cor_fundo)

    tk.Label(win, text="ID da nota:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)
    entrada_id = tk.Entry(win, width=25, font=("Arial", 12))
    entrada_id.pack(pady=5)

    tk.Label(win, text="Novo valor:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)
    entrada_novo = tk.Entry(win, width=25, font=("Arial", 12))
    entrada_novo.pack(pady=5)

    def atualizar():
        _id = entrada_id.get().strip()
        novo = entrada_novo.get().strip()

        if service.atualizar_nota(_id, novo):
            win.destroy()
        else:
            messagebox.showerror("Erro", "ID não encontrado.")

    btn = tk.Button(win, text="Atualizar", width=15, command=atualizar)
    estilizar(btn)
    btn.pack(pady=10)

def janela_favoritar():
    win = tk.Toplevel(janela)
    win.title("Favoritar Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)

    tk.Label(win, text="ID da nota:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def fav():
        _id = entrada.get().strip()
        if service.favoritar_nota(_id):
            win.destroy()

    btn = tk.Button(win, text="Favoritar", width=15, command=fav)
    estilizar(btn)
    btn.pack(pady=10)

def janela_desfavoritar():
    win = tk.Toplevel(janela)
    win.title("Desfavoritar Nota")
    win.geometry("300x180")
    win.config(bg=cor_fundo)

    tk.Label(win, text="ID da nota:", bg=cor_fundo, fg="white",
             font=("Arial", 12)).pack(pady=10)

    entrada = tk.Entry(win, width=25, font=("Arial", 12))
    entrada.pack(pady=5)

    def desfav():
        _id = entrada.get().strip()
        service.desfavoritar_nota(_id)
        win.destroy()

    btn = tk.Button(win, text="Remover Favorito", width=15, command=desfav)
    estilizar(btn)
    btn.pack(pady=10)



janela = tk.Tk()
janela.title("Sistema de notas rápidas")
janela.geometry("400x450")
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


btn_adicionar = tk.Button(tela_inicial, text="ADICIONAR NOTAS", width=20, height=2,
                          command=janela_adicionar)
estilizar(btn_adicionar)
btn_adicionar.pack(pady=5)

btn_listar = tk.Button(tela_inicial, text="LISTAR NOTAS", width=20, height=2,
                       command=janela_listar)
estilizar(btn_listar)
btn_listar.pack(pady=5)

btn_remover = tk.Button(tela_inicial, text="REMOVER NOTAS", width=20, height=2,
                        command=janela_remover)
estilizar(btn_remover)
btn_remover.pack(pady=5)

btn_atualizar = tk.Button(tela_inicial, text="ATUALIZAR NOTA", width=20, height=2,
                          command=janela_atualizar)
estilizar(btn_atualizar)
btn_atualizar.pack(pady=5)

btn_favoritar = tk.Button(
    tela_inicial, text="FAVORITAR NOTA",
    width=20, height=2,
    command=janela_favoritar
)
estilizar(btn_favoritar)
btn_favoritar.pack(pady=5)

btn_desfavoritar = tk.Button(
    tela_inicial, text="DESFAVORITAR NOTA",
    width=20, height=2,
    command=janela_desfavoritar
)
estilizar(btn_desfavoritar)
btn_desfavoritar.pack(pady=5)

janela.mainloop()
