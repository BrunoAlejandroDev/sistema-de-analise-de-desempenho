from aluno import Aluno
from pilha import Pilha
from fila import Fila
from arvore_avl import ArvoreAVL

# aluno1 = Aluno(10, 'Bruno')
# aluno1.adicionar_nota(8.5)
# aluno1.adicionar_nota(9.0)
# aluno1.adicionar_falta(2)

# aluno2 = Aluno(20, 'Alicia')
# aluno2.adicionar_nota(8)
# aluno2.adicionar_nota(9.4)
# aluno2.adicionar_falta(1)

# aluno3 = Aluno(30, 'Joaquim')

# print(aluno1)

#* ============ TESTE DA PILHA ==============
# pilha_teste = Pilha()
# print(f'Pilha vazia? {pilha_teste.is_empty()}')
# print(f'Tamanho da pilha: {len(pilha_teste)}')

# print('\nEmpilhando 10, 20, 30')
# pilha_teste.push(10)
# pilha_teste.push(20)
# pilha_teste.push(30)

# print(pilha_teste)
# print(f"Tamanho da pilha: {len(pilha_teste)}")
# print(f"Elemento no topo (peek): {pilha_teste.peek()}")

# print('Desempilhar elementos')
# while not pilha_teste.is_empty():
#     elemento_removido = pilha_teste.pop()
#     print(f'removido: {elemento_removido}')
    
# print(f'Pilha vazia? {pilha_teste.is_empty()}')

#* ============ TESTE DA FILA ==============
# fila_teste = Fila()
# print(f'Fila vazia? {fila_teste.is_empty()}')
# print(f'Tamanho da Fila: {len(fila_teste)}')

# # adicionar elementos na fila
# print('\nAdicionando elementos')
# fila_teste.enqueue(10)
# fila_teste.enqueue(20)
# fila_teste.enqueue(30)

# print(f'Fila atual: {fila_teste}')
# print(f'Fila vazia? {fila_teste.is_empty()}')
# print(f'Tamanho da Fila: {len(fila_teste)}')

# while not fila_teste.is_empty():
#     elemento_removido = fila_teste.dequeue()
#     print(f'removido: {elemento_removido}')
    
# print(f'Fila vazia? {fila_teste.is_empty()}')

#* ============ TESTE DOS PERCURSOS DA ARVORE ==============
# arvore_de_aluno = ArvoreAVL()
# print("Inserindo alunos na árvore")
# arvore_de_aluno.insert(aluno1.matricula, aluno1)
# arvore_de_aluno.insert(aluno2.matricula, aluno2)
# arvore_de_aluno.insert(aluno3.matricula, aluno3)
# print("Alunos inseridos com sucesso!")

# print('Testando os percursos')
# arvore_de_aluno.in_order()
# arvore_de_aluno.pre_order()
# arvore_de_aluno.post_order()

#* ============ TESTE DO BALANCEAMENTO DA ARVORE ==============
# arvore_de_aluno.pre_order()

#* ============ TESTE DA REMOÇÃO DA ARVORE ==============
arvore_teste_remocao = ArvoreAVL()
arvore_teste_remocao.insert(20, Aluno(20, "Roberto"))
arvore_teste_remocao.insert(10, Aluno(10, "Ana"))
arvore_teste_remocao.insert(30, Aluno(30, "Carlos"))

arvore_teste_remocao.insert(40, Aluno(40, "Daniel"))
    
print("\narvore completa antes da remocao - pre-order")
arvore_teste_remocao.pre_order()

#* Testando a remoção de um nó
print('\nRemocao')
arvore_teste_remocao.remover(10)

print('\narvore apos a remocao - pre-order')
arvore_teste_remocao.pre_order()