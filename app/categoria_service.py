from app.conexao import rds

def adicionar_categoria(categoria):
    id_novo = rds.incr('id_guardado')
    chave_tipo = f"tipo:{id_novo}"
    rds.set(chave_tipo, categoria)


def listar_categoria():
    ids = rds.keys("tipo:*")
    for id in ids:
        valor = rds.get(id)
        print(id, valor)

def buscar_categoria():
    ...

def remover_categoria():
    ...

def atualizar_categoria():
    ...