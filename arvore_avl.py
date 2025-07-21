
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
            
        #* Passo 3: atualizar a altura do nó (apos desenvolvimento da função de altura e fator de balanceamento)
        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))
        
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
        
    #* ===== METODOS DE PERCURSO =====
    def in_order(self):
        '''
        Realiza o processo de percurso a partir da raiz
        '''
        print('Percurso Em-Ordem (In-Order)')
        self._in_order(self.raiz)
        
    def _in_order(self, no_atual):
        #* Passo 1: verificar se o no existe
        if no_atual is not None:
            
            #* Passo 2: chamada recursiva para a esquerda
            self._in_order(no_atual.esquerda)
            
            #* Passo 3: chamada recursiva para o proprio no
            print(no_atual.aluno)
            
            #* Passo 4: chamada recursiva para o no da direita
            self._in_order(no_atual.direita)
        
    def pre_order(self):
        '''
        Inicia o percurso em pré-ordem a partir da raiz.
        '''
        print('Percurso Pré-Ordem (Pre-Order)')
        self._pre_order(self.raiz)
    
    def _pre_order(self, no_atual):
        #* Passo 1: verificar se o no existe
        if no_atual is not None:
            
            #* Passo 2: chamada recursiva para o proprio no
            print(no_atual.aluno)
            
            #* Passo 3: chamada recursiva para a esquerda
            self._pre_order(no_atual.esquerda)
            
            #* Passo 4: chamada recursiva para o no da direita
            self._pre_order(no_atual.direita)
        
    def post_order(self):
        '''
        Inicia o percurso em pós-ordem a partir da raiz.
        '''
        print("Percurso Pós-Ordem (Post-Order)")
        self._post_order(self.raiz)
        
    def _post_order(self, no_atual):
        #* Passo 1: verificar se o no existe
        if no_atual is not None:
            
            #* Passo 2: chamada recursiva para a esquerda
            self._post_order(no_atual.esquerda)
            
            #* Passo 3: chamada recursiva para o no da direita
            self._post_order(no_atual.direita)
            
            #* Passo 4: chamada recursiva para o proprio no
            print(no_atual.aluno)     
            
    #* ===== METODOS DE VERIFICAR ALTURA E FATOR DE BALANCEAMENTO ===== 
    
    #* Metodo _get_altura
    def _get_altura(self, no):
        #* Passo 1: verificar se o no é nulo
        if not no:
            return 0 #* caso o nó não exista, retorna 0
        
        return no.altura #* caso o nó exista, retorna a altura do nó
    
    #* Metodo de fator de balanceamento
    def _get_fator_balanceamento(self, no):
        #* Passo 1: verificar se o nó é nulo
        if not no:
            return 0
        
        #* Passo 2: calcular o fator de balanceamento com base na função de altura
        return self._get_altura(no.direita) - self._get_altura(no.esquerda)