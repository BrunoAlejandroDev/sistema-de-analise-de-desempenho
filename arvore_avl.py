
#* Importacoes
from avl_node import AvlNode
from aluno import Aluno

class ArvoreAVL:
    """
    Implementa a estrutura de dados Árvore AVL.
    Esta classe gerenciará os nós, incluindo inserção, remoção, busca e balanceamento.
    """
    def __init__(self):
        self.raiz = None
        
    def insert(self, chave, aluno):
        '''
        Metodo publico de inserção de um novo nó na arvoré
        '''
        self.raiz = self._insert(self.raiz, chave, aluno)
            
    def _insert(self, no_atual, chave, aluno):
        #* Passo1: caso base -> encontrar lugar vazio para a inserção do novo nó
        if no_atual is None:
            return AvlNode(chave, aluno)
        
        #* Passo 2: Passos recursivos
        if chave < no_atual.chave: #* o no atual recebe novamente seu filho da esquerda
            no_atual.esquerda = self._insert(no_atual.esquerda, chave, aluno)
        else:
            no_atual.direita = self._insert(no_atual.direita, chave, aluno)
        
        return no_atual
    
    def buscar(self, chave):
        '''
        Método público para buscar um aluno pela chave
        '''
        #* Passo 1: caso base
        return self._buscar(self.raiz, chave)
    
    def _buscar(self, no_atual, chave):
        #* Passo 1: caso base -> verificar se matricula é none ou se é a buscada
        if no_atual is None or no_atual.chave == chave:
            return no_atual.aluno if no_atual else None
        
        #* Passo 2: passo recursivo
        if chave < no_atual.chave:
            return self._buscar(no_atual.esquerda, chave)
        else:
            return self._buscar(no_atual.direita, chave)