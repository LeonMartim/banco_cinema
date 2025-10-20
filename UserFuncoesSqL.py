from FuncoesSqL import *

def menu():
    print("\n-------- Menu --------")
    print("1 - Inserir filme")
    print("2 - Listar filmes")
    print("3 - Listar Personagem")
    print("4 - Deletar Filme")
    print("0 - Sair")

def main():
    conn = colectar()
    cursor = conn.cursor()

    while True:
        menu()
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            nome = input("Nome do filme: ")
            data = input("Data de lançamento (YYYY-MM-DD): ")
            orcamento = float(input("Orçamento: "))
            tempo = int(input("Tempo (minutos): "))

            inserir_filme(cursor, nome, data, orcamento, tempo)
            conn.commit()
            print("Filme inserido com sucesso!")

        elif opcao == "2":
            filmes = listar_filmes(cursor)
            print(f"{'ID':<5} {'Nome':<25} {'Lançamento':<15} {'Orçamento':<15} {'Tempo (min)':<12}")
            print("-" * 80)
            for f in filmes:
                print(f"{f[0]:<5} {f[1]:<25} {str(f[2]):<15} {str(f[3]):<15} {str(f[4]):<12}")

        elif opcao == "3":
            personagens = listar_personagem(cursor)
            print(f"{'ID_per':<10} {'Id_fil':<10} {'Id_Ator':<15} {'Nome personagem':<20} {'Cache'}")
            print("-" * 70)
            for p in personagens:
                print(f'{p[0]:<10} {p[1]:<10} {p[2]:<15} {str(p[3]):<20} {str(p[4])}')
        
        elif opcao == "4":
            filmes = listar_filmes(cursor)
            print(f"{'ID':<5} {'Nome':<25} {'Lançamento':<15} {'Orçamento':<15} {'Tempo (min)':<12}")
            print("-" * 80)
            for f in filmes:
                print(f"{f[0]:<5} {f[1]:<25} {str(f[2]):<15} {str(f[3]):<15} {str(f[4]):<12}")

            cod = int(input("\nDigite o código do filme para deletar: "))
            if deletar_filme(cursor, cod):
                conn.commit()
                print("Filme deletado com sucesso!")
            else:
                print("Erro de integridade referencial! Esse filme ainda pode estar sendo referenciado.")
                print("Para evitar erro de integridade referencial, primeiro exclua os Personagens associados.\n")

                personagens = listar_personagem(cursor)
                print(f"{'ID personagem':<18} {'Id filme':<25} {'Nome personagem':<25} {'Cache'}")
                print("-" * 60)
                for p in personagens:
                    print(f'{p[0]:<18} {p[1]:<25} {p[2]:<25} {str(p[3])}')

                cod_personagem = int(input("\nDigite o código do personagem para deletar: "))
                if deletar_personagem(cursor, cod_personagem):
                    conn.commit()
                    print("Personagem deletado com sucesso!")
                else:
                    print("Erro: personagem não encontrado.")

        elif opcao == "0":
            break 

        else:
            print("Opcao inválida, tente novamente.")
        
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()



            