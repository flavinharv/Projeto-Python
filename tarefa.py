import os
import json

class Tarefa:
    __arquivo = 'tarefa.json'

    def __init__(self, titulo, descricao, prioridade, dataInicio, dataFim, status):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__dataInicio = dataInicio
        self.__dataFim = dataFim
        self.__status = status

    @classmethod
    def cadastrarTarefa(cls):
        """ Método que tem como função cadastrar tarefa e salvar em arquivo json. """
        print('\n📌 Insira as informações para cadastrar a tarefa:\n')

        titulo = input('☑️  Título: ')
        if not titulo:
            print('\n⚠️  \033[91mO título não pode ser vazio!\033[0m ⚠️\n')
            return
        
        descricao = input('☑️  Descrição: ')
        if not descricao or len(descricao) < 10:
            print('\n⚠️   \033[91mDescrição muito pequena!\033[0m ⚠️')
            return 
        
        prioridade = input('☑️  Prioridade: ')

        dataInicio = input('☑️  Data de início: ')
        dataFim = input('☑️  Data de fim: ')
        if not dataInicio or not dataFim:
            print('\n⚠️   \033[91mDatas incorretas!\033[0m ⚠️')
            return 
        
        status = input('☑️  Status: ')

        tarefa = {
            'Título': titulo,
            'Descrição': descricao,
            'Prioridade': prioridade,
            'Data de início': dataInicio,
            'Data de fim': dataFim,
            'Status': status
        }

        if not os.path.exists(cls.__arquivo):
            with open(cls.__arquivo, 'w', encoding='UTF-8') as arquivo:
                json.dump([], arquivo)

        with open(cls.__arquivo, 'r+', encoding='UTF-8') as arquivo:
            try:
                t = json.load(arquivo)  

            except json.JSONDecodeError:
                t = [] 

            t.append(tarefa)  

            with open(cls.__arquivo, 'w', encoding='UTF-8') as arquivo:
                json.dump(t, arquivo, ensure_ascii=False, indent=4)

            print('\n\033[91mTarefa cadastrada com sucesso!\033[0m ✔')

    @classmethod
    def listarTarefas(cls):
        """ Método usado para percorrer a lista de tarefas e imprimir cada uma delas. """
        if not os.path.exists(cls.__arquivo):
            print('\n\033[91mNenhuma tarefa cadastrada!\033[0m ❌')
            return

        with open(cls.__arquivo, 'r', encoding='UTF-8') as arquivo:
            try:
                tarefas = json.load(arquivo)  

                if not tarefas:
                    print('\033[91mNenhuma tarefa cadastrada!\033[0m  ❌')
                    return
                
                for index, tarefa in enumerate(tarefas, start=1):
                    print(f'\n\033[91m\n 📌 {index}º Tarefa\033[0m')
                    print('-' * 50)
                    print(f'''
                    Título: {tarefa['Título']}
                    Descrição: {tarefa['Descrição']}
                    Prioridade: {tarefa['Prioridade']}
                    Data de Início: {tarefa['Data de início']}
                    Data de Fim: {tarefa['Data de fim']}
                    Status: {tarefa['Status']}
                    ''')

            except json.JSONDecodeError:
                print('\033[91mErro ao ler o arquivo. O arquivo está vazio ou corrompido!\033[0m ☠️\n')

    @classmethod
    def concluirTarefa(cls):
        """ Método usado para concluir uma tarefa pendente. """
        num = int(input('\n 📌 Digite o número da tarefa que deseja concluir: '))

        with open(cls.__arquivo, 'r+', encoding='UTF-8') as arquivo:
            tarefas = json.load(arquivo)

            if num < 1 or num > len(tarefas):
                print("\033[91mTarefa inválida\033[0m ❌")

            tarefas[num - 1]['Status'] = 'Concluída'
     
            arquivo.seek(0) 
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

            print(f"\nTarefa '\033[91m{tarefas[num - 1]['Título']}\033[0m' concluída com sucesso!\033[3;34m ✔")

    @classmethod
    def excluirTarefa(cls):
        """ Método que tem como função excluir uma tarefa cadastrada na agenda."""
        num = int(input('\n 📌 Digite o número da tarefa que deseja excluir: '))

        if not os.path.exists(cls.__arquivo):
            print('\033[91mNenhuma tarefa cadastrada!\033[0m ❌')
            return

        with open(cls.__arquivo, 'r+', encoding='UTF-8') as arquivo:
            tarefas = json.load(arquivo)

        if num < 1 or num > len(tarefas):
            print('\033[91mTarefa inválida!\033[0m ❌')

        tarefa_removida = tarefas.pop(num - 1)
        
        with open(cls.__arquivo, 'w', encoding='UTF-8') as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

        print(f"\nTarefa '\033[91m{tarefa_removida['Título']}\033[0m' excluída com sucesso! ✔")