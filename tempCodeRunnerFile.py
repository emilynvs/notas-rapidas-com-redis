from app import notas_service as service

def main():

    realizar_loop = True

    while(realizar_loop):
        print("-=" *20)
        print("MENU")
        print("-=" *20)

        print("1 - Adicionar nota")
        print("2 - Listar tudo")
        print("3 - Remover nota")        
        print("4 - Atualizar nota")
        print("5 - Encerrar")
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            texto = input("Digite sua nota")
            service.adicionar_nota(texto)
        elif opcao == 2:
            service.listar_tudo()
        elif opcao == 3:
            service.remover_nota()
        elif opcao == 4:
            service.atualizar_nota()
        elif opcao == 5:
            realizar_loop = False
        else:
            print("Escolha inválida")
    print("Serviço finalizado. Até a próxima")

if __name__ == "__main__":
    main()