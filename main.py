from aluno import Aluno
from pilha import Pilha

# aluno1 = Aluno(536498, 'Bruno')
# aluno1.adicionar_nota(8.5)
# aluno1.adicionar_nota(9.0)
# aluno1.adicionar_falta(2)

# print(aluno1)

#* ============ TESTE DA PILHA ==============
pilha_teste = Pilha()
print(f'Pilha vazia? {pilha_teste.is_empty()}')
print(f'Tamanho da pilha: {len(pilha_teste)}')

print('\nEmpilhando 10, 20, 30')
pilha_teste.push(10)
pilha_teste.push(20)
pilha_teste.push(30)

print(pilha_teste)
print(f"Tamanho da pilha: {len(pilha_teste)}")
print(f"Elemento no topo (peek): {pilha_teste.peek()}")

print('Desempilhar elementos')
while not pilha_teste.is_empty():
    elemento_removido = pilha_teste.pop()
    print(f'removido: {elemento_removido}')
    
print(f'Pilha vazia? {pilha_teste.is_empty()}')