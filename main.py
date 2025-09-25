from tarefa import Tarefa
import time

def menu():
    while True:
        print('='*50)
        print('📅 AGENDA DE TAREFAS 📅'.center(50))
        print('\033[3;34mTarefas sob controle, vida sem estresse!\033[0m'.center(60))
        print('''\n
        ---------📚 MENU 📚---------
        1️⃣  Cadastrar Tarefa
        2️⃣  Listar Tarefa
        3️⃣  Concluir Tarefa
        4️⃣  Excluir Tarefa
        5️⃣  Sair
            
    ''')
        
        op = input("Escolha uma opção do menu: ")

        if op == '1':
            print("-"*50)
            print('\033[3;34mCadastrando...\033[0m')
            print("-"*50)
            Tarefa.cadastrarTarefa()
        
        
        elif op == '2':
            print('-' * 50)
            print('\033[3;34mListando...\033[0m')
            print('-' * 50)
            Tarefa.listarTarefas()

        elif op == '3':
            Tarefa.concluirTarefa() 

        elif op == '4':
            Tarefa.excluirTarefa()

        elif op == '5':
            print('-' * 50)
            print('\033[3;34mSaindo do programa...\033[0m')
            print('\n\033[3;34mPlanejar hoje é garantir as oportunidades de amanhã!\033[0m'.center(60))
            print('-' * 50)
            break

        else:
            print('\n\033[91mOpção inválida!\033[0m ❌')

if __name__ == '__main__':
    menu()