
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