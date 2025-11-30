from conexao import rds

def adicionar_nota(texto):
    novo_id = rds.incr('contador')
    chave_nota = f"nota:{novo_id}"
    rds.set(chave_nota, texto)


def listar_tudo():
    ids = rds.keys("nota:*")
    if not ids:
        print("Ainda não há notas adicionadas")
        return
    for id in ids:
        valor = rds.get(id)
        print(id, valor)

def remover_nota():
    listar_tudo()
    remover_id = int(input("Digite o número da nota que deseja remover: "))
    chave = f"nota{remover_id}"
    if not rds.exists(chave):
        print("Não existe essa nota")
        return
    rds.delete(chave)
    print("Nota deletada")


def atualizar_nota():
    listar_tudo()
    id_nota = int(input("Digite o número da nota que deseja atulizar: "))
    chave = f"nota{id_nota}"
    
    if not rds.exists(chave):
        print("Não existe essa nota")
        return
    
    novo_texto = input("Digite o texto para atualizar a nota: ")
    rds.set(f"nota:{id_nota}", novo_texto)
    print("Nota atualizada")

def apagar_tudo():
    resposta = input("Tem certeza que deseja apagar TODAS as notas?")
    if resposta in 'sS':
        rds.flushdb()
        print("Todas as notas foram apagadas")
    else:
        print("Processo cancelado")