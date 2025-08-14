
#* Importacoes de arquivo
from sadhe.models.node import Node

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
        novo_no = Node(dado) #* cria um novo no
        novo_no.proximo = self.topo
        self.topo = novo_no
        self._tamanho += 1
    
    def pop(self):
        '''
        Remove um elemento do topo da pilha
        '''
        #* Passo 1: verificar se a pilha esta vazia
        if self.is_empty():
            raise IndexError('Pilha vazia')
        
        #* Passo 2: salvar o elemento que sera removido
        elemento_removido = self.topo.dado
        
        #* Passo 3: stualizar o topo da pilha e o tamanho dela
        self.topo = self.topo.proximo
        self._tamanho -= 1
        
        #* Passo 4: retorna o elemento removido
        return elemento_removido 
    
    def peek(self):
        '''
        Retorna o elemento do topo da pilha mas sem remover o elemento
        '''
        #* Passo 1: verificar se a pilha esta vazia
        if self.is_empty():
            raise IndexError('Pilha vazia')
        
        #* Passo 2: retornar o dado do topo 
        return self.topo.dado
    
    def __len__(self):
        '''
        Habilita o uso da função len() na pilha
        '''
        return self._tamanho
    
    def __str__(self):
        lista_elementos = []
        
        no_atual = self.topo
        while no_atual:
            lista_elementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
            
        return ' -> '.join(lista_elementos)