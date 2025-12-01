from conexao import rds
import time
from datetime import datetime

def formatar_timestamp(ts):
    return datetime.fromtimestamp(float(ts)).strftime("%d/%m/%Y %H:%M:%S")

def adicionar_nota(texto):
    novo_id = rds.incr('contador')
    chave_nota = f"nota:{novo_id}"
    rds.hset(chave_nota, mapping={
        "texto": texto,
        "criado_em": time.time(),
        "atualizado_em": time.time()
    })



def listar_tudo():
    chaves = rds.keys("nota:*")
    notas = []

    if not chaves:
        return []

    for chave in chaves:
        # Decodifica chave se vier como bytes
        if isinstance(chave, bytes):
            chave = chave.decode("utf-8")

        # Garante que a chave é HASH antes de chamar HGETALL
        tipo = rds.type(chave)
        if isinstance(tipo, bytes):
            tipo = tipo.decode()

        if tipo != "hash":
            continue  # ignora chave inválida

        dados = rds.hgetall(chave)

        # Se decode_responses=False, converte bytes → string
        dados = {
            (k.decode() if isinstance(k, bytes) else k):
            (v.decode() if isinstance(v, bytes) else v)
            for k, v in dados.items()
        }

        texto = dados.get("texto", "")
        criado_em = formatar_timestamp(dados.get("criado_em", "0"))
        atualizado_em = formatar_timestamp(dados.get("atualizado_em", "0"))

        id_nota = chave.split(":")[1]

        notas.append((id_nota, texto, criado_em, atualizado_em))

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
    rds.hset(chave, "texto", novo_texto)
    rds.hset(chave, "atualizado_em", time.time())
    return True


def apagar_tudo():
    resposta = input("Tem certeza que deseja apagar TODAS as notas?")
    if resposta in 'sS':
        rds.flushdb()
        print("Todas as notas foram apagadas")
    else:
        print("Processo cancelado")

def favoritar_nota(id_nota):
    chave = f"nota:{id_nota}"
    if not rds.exists(chave):
        return False
    
    rds.sadd("favoritas", id_nota)
    return True

def desfavoritar_nota(id_nota):
    rds.srem("favoritas", id_nota)
    return True

def listar_favoritas():
    favoritos = rds.smembers("favoritas")
    notas = []

    for f in favoritos:
        if isinstance(f, bytes):
            f = f.decode()

        chave = f"nota:{f}"
        dados = rds.hgetall(chave)

        if not dados:
            continue

        texto = dados.get(b"texto", b"").decode()
        criado_em = formatar_timestamp(dados.get(b"criado_em", b"0"))
        atualizado_em = formatar_timestamp(dados.get(b"atualizado_em", b"0"))

        notas.append((f, texto, criado_em, atualizado_em))

    return notas