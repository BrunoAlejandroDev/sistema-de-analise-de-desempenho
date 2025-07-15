from node import Node

class Pilha:
    '''
    Implementação da estrutura de dados Pilha a partir de nós encadeados
    '''
    def __init__(self):
        self.topo = None #* estado inicial da pilha será vazia
        self._tamanho = 0
        
    def is_empty(self):
        '''
        Verifica se a pilha está vazia
        '''
        return self.topo is None
        
    #* Metodo para puxar um elemento da lista
    def push(self, dado):
        '''
        Adiciona um elemento ao topo da pilha
        '''
        novo_no = Node(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self._tamanho += 1
            