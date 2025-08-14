class Node:
    '''
    Representa um nó na estrutura de dados encadeada. Cada nó aponta para o próximo.
    '''
    def  __init__(self, dado):
        self.dado = dado #* dado armazenado pelo nó
        self.proximo = None #* ponteiro de referencia para o proximo elemento