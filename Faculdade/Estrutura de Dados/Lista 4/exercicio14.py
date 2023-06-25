class Node:

    def __init__(self, __id, name, priority, wait, nxt=None):
        self.id = __id
        self.name = name
        self.priority = priority
        self.wait = wait
        self.nxt = nxt


class TaskManager:

    def __init__(self):
        self.tail = None
        self.head = None

    def insert_process(self, __id, name, priority, wait):
        new_process = Node(id, name, priority, wait)
        if self.head is None:
            self.head = new_process
            self.tail = new_process
        else:
            mem = self.tail
            self.tail = new_process
            self.tail.nxt = mem
        return

    def kill(self):

        if self.head is None:
            print('Não há processos na fila.')
            return
        else:
            maior = self.tail.wait
            itr = self.tail
            while itr:
                if itr.wait > maior:
                    maior = itr.wait
                itr = itr.nxt

            itr = self.tail
            while itr.nxt.wait != maior:
                itr = itr.nxt
            itr.nxt = itr.nxt.nxt
        return

    def execute(self):
        if self.head is None:
            print('Não há processos na fila.')
        else:
            itr = self.tail
            while itr.nxt != self.head:
                itr = itr.nxt
            itr.nxt = None
            self.head = itr
        return

    def show_process_list(self):
        itr = self.tail
        queue = ''
        if self.head is None:
            print('A fila está vazia.')
        else:
            while itr:
                queue = ' <- ' + str(itr.name) + queue
                itr = itr.nxt
            queue = '[' + queue[4:] + ']'
        return str(queue)


print('Tem um erro nesse programa que não consegui resolver agora, mas vou resolver essa porcaria e colocar no git\n')

task_manager = TaskManager()

print('Gerenciador de tarefas:\n'
      '1 - Matar processo mais pesado\n'
      '2 - Executar um processo\n'
      '3 - Mostrar lista de processos\n'
      '4 - Exibir menu novamente\n'
      '0 - Encerrar programa\n')

task_manager.insert_process(101, "A", 1, 10)
task_manager.insert_process(102, "B", 2, 20)
task_manager.insert_process(103, "C", 1, 15)
task_manager.insert_process(104, "D", 3, 12)

while True:

    opcao = input('Insira a opção desejada: ')

    try:
        opcao = int(opcao)
    except ValueError:
        print('Caractere inválido.')

    if opcao == 1:
        task_manager.kill()
        print('O processo mais pesado foi encerrado.')

    elif opcao == 2:
        task_manager.execute()
        print('Processo executado.')

    elif opcao == 3:
        print(f'Gerenciador de tarefas: {task_manager.show_process_list()}')

    elif opcao == 4:
        print('Gerenciador de tarefas:\n'
              '1 - Matar processo mais pesado\n'
              '2 - Executar um processo\n'
              '3 - Mostrar lista de processos\n'
              '4 - Exibir menu novamente\n'
              '0 - Encerrar programa\n')
        continue

    elif opcao == 0:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida.\n')
        continue

print('powered by ggOS')
