import redis

rds = redis.Redis(host='localhost', port=6379, db=0)


def adicionar_nota(texto):
    ids = rds.keys("nota:*")
    novo_id = len(ids) + 1

    chave_nota = f"nota:{novo_id}"

    rds.set(chave_nota, texto)

adicionar_nota("Comprar melancia")



