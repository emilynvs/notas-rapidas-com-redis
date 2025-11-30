from conexao import rds

def adicionar_nota(texto):
    novo_id = rds.incr('contador')
    chave_nota = f"nota:{novo_id}"
    rds.set(chave_nota, texto)


def listar_tudo():
    ids = rds.keys("nota:*")
    for id in ids:
        valor = rds.get(id)
        print(id, valor)

def remover_nota():
    listar_tudo()
    remover_id = int(input("Digite o número da nota que deseja remover: "))
    rds.delete(f"nota:{remover_id}")
    print("Nota deletada")


def atualizar_nota():
    listar_tudo()
    id_nota = int(input("Digite o número da nota que deseja atulizar: "))
    novo_texto = input("Digite o texto para atualizar a nota: ")
    rds.set(f"nota:{id_nota}", novo_texto)

    print("Nota atualizada")


def buscar_nota():
    ...
    
    
    
    