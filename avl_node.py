# from aluno import Aluno

class AvlNode:
    """
    Representa um nó em uma Árvore AVL.
    Contém a chave de ordenação, o dado completo, referências para os filhos
    e o atributo 'altura' para o cálculo do balanceamento.
    """
    def __init__(self, chave, aluno):
        self.chave = chave #* matricula do aluno -> ordenar a arvore
        self.aluno = aluno #* objeto aluno completo
        self.esquerda = None
        self.direita = None
        self.altura = 1 #* a altura de um novo nó (folha) é sempre 1
        
    def __str__(self):
        return f"Chave (matricula): {self.chave} (Aluno: {self.aluno.nome})"