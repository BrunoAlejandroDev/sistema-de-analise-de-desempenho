
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
        
        #* Passo 4: Verificar fator de balanceamento
        balanceamento = self._get_fator_balanceamento(no_atual)
        
        #* Passo 5: Caso nó esteja desbalanceado, fazer 4 verificações
        #* Caso 1: rotação simples a direita
        if balanceamento < -1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)
        
        #* Caso 2: rotação simples a esquerda
        if balanceamento > 1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)
        
        #* Caso 3: rotação dupla esquerda-direita
        if balanceamento < -1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)
        
        #* Caso 4: rotação dupla direita-esquerda
        if balanceamento > 1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
        
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
        '''
        Método para verificar a altura de um nó
        '''
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
    
    #* ===== METODOS DE ROTAÇÃO (DIREITA E ESQUERDA) ===== 
    def _rotacao_direita(self, z):
        '''
        Método para executar uma rotação à direita na subárvore com raiz z
        '''
        #* Passo 1: identifica os nós que devem subir (y) e os nós que serão movidos (T3)
        y = z.esquerda
        T3 = y.direita
        
        #* Passo 2: executar a rotação
        y.direita = z
        z.esquerda = T3
        
        #* Passo 3: atualiza as alturas
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        
        #* Passo 4: retornar a nova raiz da subarvore
        return y
    
    def _rotacao_esquerda(self, z):
        '''
        Método para executar uma rotação à esquerda na subárvore com raiz z.
        '''
        #* Passo 1: identifica os nós que devem subir (y) e os nós que serão movidos (T2)
        y = z.direita
        T2 = y.esquerda

        #* Passo 2: executar a rotação
        y.esquerda = z
        z.direita = T2

        #* Passo 3: atualiza as alturas
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        #* Passo 4: retornar a nova raiz da subarvore
        return y
    
    #* ===== METODO DE REMOÇÃO =====
    def remover(self, chave):
        '''
        Método público para remover um nó da árvore por meio da matrícula do aluno (chave)
        '''
        print('Remover aluno via matricula')
        self.raiz = self._remover(self.raiz, chave)
        
    def _get_menor_no_subarvore_direita(self, no):
        '''
        Método para encontrar o menor nó da subárvore da direita
        '''
        if no is None or no.esquerda is None:
            return no
        
        return self._get_menor_no_subarvore_direita(no.esquerda)
    
    def _remover(self, no_atual, chave):
        '''
        Método recursivo para auxiliar o método de remoção público e balancear a árvore
        '''
        #* Verificar se o nó atual existe
        if not no_atual:
            print(f'Erro: Aluno com matricula {chave} não encontrado')
            return no_atual
        
        #* Buscar Nó que será removido
        if chave < no_atual.chave: #* Caso 1: verificar a esquerda
            no_atual.esquerda = self._remover(no_atual.esquerda, chave)
        elif chave > no_atual.chave: #* Caso 2: verificar a direita
            no_atual.direita = self._remover(no_atual.direita, chave)
        
        #* Nó encontrado, começar remoção
        else:
            #* Caso 1 e 2 -> nó com 0 ou 1 filho    
            if no_atual.esquerda is None:
                temp = no_atual.direita
                print(f'-- removendo aluno com matricula: {no_atual.chave}')
                no_atual = None #* retira a referência do nó
                return temp
            
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                print(f'-- removendo aluno com matricula: {no_atual.chave}')
                no_atual = None #* retira a referencia do nó
                return temp
            
            #* Caso 3 -> nó com 2 filhos
            print(f'-- removendo aluno com matricula: {no_atual.chave}')
            temp = self._get_menor_no_subarvore_direita(no_atual.direita)
            no_atual.chave = temp.chave #* copiar dados do proximo nó
            no_atual.aluno = temp.aluno #* copiar dados do proximo nó
            no_atual.direita = self._remover(no_atual.direita, temp.chave)

            print('-- remocao concluida com sucesso.')
                   
        #* Rebalancear a arvore apos remoção
        if no_atual is None:
            return no_atual
        
        #* Passo 1: atualizar a altura do nó (apos desenvolvimento da função de altura e fator de balanceamento)
        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))
        
        #* Passo 2: Verificar fator de balanceamento
        balanceamento = self._get_fator_balanceamento(no_atual)
        
        #* Passo 3: Caso nó esteja desbalanceado, fazer 4 verificações
        
        #* Caso 1: rotação simples a direita (esquerda-esquerda)
        if balanceamento < -1 and self._get_fator_balanceamento(no_atual.esquerda) <= 0:
            print('rotacao direita simples')
            return self._rotacao_direita(no_atual)
        
        #* Caso 2: rotação simples a esquerda (direita-direita)
        if balanceamento > 1 and chave > self._get_fator_balanceamento(no_atual.direita) >= 0:
            print('rotacao esquerda simples')
            return self._rotacao_esquerda(no_atual)
        
        #* Caso 3: rotação dupla esquerda-direita
        if balanceamento < -1 and self._get_fator_balanceamento(no_atual.esquerda) > 0:
            print('rotacao dupla esquerda-direita')
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)
        
        #* Caso 4: rotação dupla direita-esquerda
        if balanceamento > 1 and self._get_fator_balanceamento(no_atual.direita) < 0:
            print('rotacao dupla direita-esquerda')
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
        
        return no_atual
    
    #* ===== IMPRIMIR ARVORE =====
    def display(self):
        '''
        Mostra a estrutura da árvore de forma visual
        '''
        print("Estrutura visual da arvore")
        self._display(self.raiz, 0)
        print("---------------------------------")

    def _display(self, no, level):
        if no is not None:
            #* Imprime a subárvore da direita primeiro (para que fique no topo)
            self._display(no.direita, level + 1)
            
            #* Imprime o nó atual com indentação
            print(' ' * 4 * level + '->', no.chave)
            
            #* Imprime a subárvore da esquerda
            self._display(no.esquerda, level + 1)