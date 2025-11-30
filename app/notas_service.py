from app.conexao import rds

def adicionar_nota(texto):
    ids = rds.keys("nota:*")
    novo_id = rds.incr('contador')
    chave_nota = f"nota:{novo_id}"
    rds.set(chave_nota, texto)

def listar_tudo():
    ids = rds.keys("nota:*")
    for id in ids:
        id_atual = rds.get(id)
        print(id, id_atual)

def remover_nota():
    listar_tudo()
    remover_id = int(input("Digite o número da nota que deseja remover: "))
    rds.delete(f"nota:{remover_id}")
    print("Nota deletada")
    listar_tudo()

def atualizar_nota():
    listar_tudo()
    id_nota = int(input("Digite o número da nota que deseja atulizar: "))
    novo_texto = input("Digite o texto para atualizar a nota: ")
    rds.set(f"nota:{id_nota}", novo_texto)

    print("Nota atualizada")
    listar_tudo()

def buscar_nota():
    ...



