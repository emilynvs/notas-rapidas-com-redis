import redis

rds = redis.Redis(host='localhost', port=6379, db=0)

def adicionar_nota(texto):
    ids = rds.keys("nota:*")
    novo_id = rds.incr('contador')

    chave_nota = f"nota:{novo_id}"

    rds.set(chave_nota, texto)

def listar_tudo():
    ids = rds.keys("nota:*")
    for id in ids:
        id_atual = rds.get(id)
        print(id.decode(), id_atual.decode())




