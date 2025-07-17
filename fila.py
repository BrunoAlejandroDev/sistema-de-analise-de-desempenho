
#* Importacoes
from node import Node

class Fila:
    '''
    Implementa uma estrutura de dados do tipo Fila (Queue) por meio de nós encadeados.
    A estrutura usa a lógica FIFO
    '''
    def __init__(self):
        self.front = None
        self.rear = None
        self._tamanho = 0
        
    def is_empty(self):
        '''
        Verifica se a fila está vazia
        '''
        return self.front is None
        
    def enqueue(self, dado):
        '''
        Adiciona um elemento ao final da fila (nó "rear")
        '''
        #* Passo 1: criar o novo dado
        novo_no = Node(dado)
        
        #* Passo 2: verifica se a fila estiver vazia. Front e rear recebem o novo dado
        if self.is_empty():
            self.front = novo_no
            self.rear = novo_no
            
        #* Passo 3: fila ja tem elementos e deve ser atualizada com novo valor
        else:
            self.rear.proximo = novo_no #* atualiza o ponteiro de referencia do ultimo elemento
            self.rear = novo_no #* atualiza o ultimo elemento da fila
        
        self._tamanho += 1
        
    def dequeue(self):
        '''
        Remove o elemento do inicio da fila e retorna seu valor
        '''
        #* Passo 1: verificar se a fila esta vazia
        if self.is_empty():
            raise IndexError('A fila está vazia')
        
        #* Passo 2: Guardar o valor do elemento no inicio da fila
        elemento_removido = self.front.dado
        
        #* Passo 3: atualizar o inicio da fila
        self.front = self.front.proximo
        
        #* Passo 4: verificar se a fila ficou vazia apos remoção
        if self.front is None:
            self.rear = None
            
        #* Atualizar o tamanho da fila 
        self._tamanho -= 1
            
        #* Passo 5: retornar o elemento removido
        return elemento_removido
    
    def peek(self):
        '''
        Retorna o elemento do inicio da fila mas sem removê-lo
        '''
        #* Passo 1: verificar se a fila está vazia
        if self.is_empty:
            raise IndexError('A fila está vazia')
        
        #* Retornar o elemento do topo
        return self.front.dado
    
    def __len__(self):
        '''
        Habilita o uso da função len() na pilha
        '''
        return self._tamanho
    
    def __str__(self):
        fila_elementos = []
        
        no_atual = self.front
        while no_atual:
            fila_elementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
            
        return ' -> '.join(fila_elementos)