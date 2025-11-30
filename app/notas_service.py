from conexao import rds


def adicionar_nota(texto: str):
    novo_id = rds.incr("contador")        # gera ID automático
    chave = f"nota:{novo_id}"
    rds.set(chave, texto)
    return novo_id


def listar_tudo():
    notas = []
    ids = sorted(rds.keys("nota:*"), key=lambda x: int(x.split(":")[1]))

    for chave in ids:
        texto = rds.get(chave)
        id_nota = chave.split(":")[1]
        notas.append((id_nota, texto))

    return notas


def remover_nota(id_nota: str):
    chave = f"nota:{id_nota}"
    if rds.exists(chave):
        rds.delete(chave)
        return True
    return False


def atualizar_nota(id_nota: str, novo_texto: str):
    chave = f"nota:{id_nota}"
    if rds.exists(chave):
        rds.set(chave, novo_texto)
        return True
    return False
