from conexao import rds

def adicionar_nota(texto):
    novo_id = rds.incr('contador')
    chave_nota = f"nota:{novo_id}"
    rds.set(chave_nota, texto)

def listar_tudo():
    ids = rds.keys("nota:*")
    notas = []

    if not ids:
        return []

    for chave in ids:
        valor = rds.get(chave)

        if isinstance(valor, bytes):
            valor = valor.decode("utf-8")

        if isinstance(chave, bytes):
            chave = chave.decode("utf-8")

        id_nota = chave.split(":")[1]

        notas.append((id_nota, valor))

    return notas



def remover_nota(id_nota):
    chave = f"nota:{id_nota}"
    if not rds.exists(chave):
        return False
    rds.delete(chave)
    return True


def atualizar_nota(id_nota, novo_texto):
    chave = f"nota:{id_nota}"
    if not rds.exists(chave):
        return False
    rds.set(chave, novo_texto)
    return True


def apagar_tudo():
    resposta = input("Tem certeza que deseja apagar TODAS as notas?")
    if resposta in 'sS':
        rds.flushdb()
        print("Todas as notas foram apagadas")
    else:
        print("Processo cancelado")
