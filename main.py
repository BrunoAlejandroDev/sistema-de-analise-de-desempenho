
#* Importacoes de arquivo
from arvore_avl import ArvoreAVL
from fila import Fila
from pilha import Pilha
from aluno import Aluno

#* Menu interativo
def exibir_menu():
    print("\n=== Sistema de Análise de Desempenho (SADHE) ===")
    print("1. Cadastrar Novo Aluno")
    print("2. Lançar Relatório de Desempenho")
    print("3. Processar Fila de Relatórios")
    print("4. Buscar Aluno por Matrícula")
    print("5. Listar Todos os Alunos (por matrícula)")
    print("6. Ver Histórico de um Aluno")
    print("7. Remover Aluno")
    print("8. Visualizar Árvore")
    print("9. Sair")
    return input("Escolha uma opção: ")

#* Execução do sistema
def main():
    #* Variaveis de acesso a estrutura do projeto
    arvore_alunos = ArvoreAVL()
    fila_relatorios = Fila()
    pilhas_historico = {}

    #* Loop de execução do sistema
    while True:
        opcao = exibir_menu().strip()

        #* Opcao 1: cadastrar aluno
        if opcao == '1':
            try:
                print('\nProcesso Atual: Cadastrar Aluno')
                matricula = int(input('- Digite a matricula: '))
                nome = input('- Digite o nome: ')

                #* Verificar se aluno já existe no sistema
                if arvore_alunos.buscar(matricula):
                    print('- Erro. Matricula já cadastrada no sistema.')
                else:
                    novo_aluno = Aluno(matricula, nome)
                    arvore_alunos.insert(matricula, novo_aluno)
                    pilhas_historico[matricula] = Pilha()
                    print(f'-- Aluno {nome} - {matricula} foi cadastrado com sucesso.')

            except ValueError:
                print('- Erro. A matricula deve ser um número')

        #* Opcao 2: Lançar relatório
        elif opcao == '2':
            try:
                print('\nProcesso Atual: Cadastrar Relatótio no Sistema')
                #* Variaveis
                matricula = int(input('- Digite a matrícula: '))
                nota = float(input('- Digite a nota a ser adicionada: '))

                #* Verificar se aluno está presente no sistema para adicionar nota
                if arvore_alunos.buscar(matricula):
                    relatorio = { #* criar estrutura do relatorio
                        'matricula' : matricula,
                        'nota' : nota
                    }
                    fila_relatorios.enqueue(relatorio) #* adiciona o relatorio na fila de processamento
                    print('-- Relatório adicionado com sucesso à fila de processamento.')
                else:
                    print(f'-- Aluno com matricula {matricula} não identificado no sistema.')

            except ValueError:
                print('- Erro. A matricula deve ser um número')

        #* Opcao 3: processar fila de relatórios cadastrados
        elif opcao == '3':
            print('\nProcesso Atual: Processar Relatórios')
            #* Verificar se existem relatorios a serem preenchidos
            if fila_relatorios.is_empty():
                print('- A fila de relatórios está vazia.')
            else:
                relatorio = fila_relatorios.dequeue()
                aluno = arvore_alunos.buscar(relatorio['matricula']) #* buscar os relatorios de um aluno com base na matricula

                if aluno: #* se aluno existir
                    pilha_relatorios_aluno = pilhas_historico[aluno.matricula]
                    
                    estado_antigo = {
                        'media' : aluno.media_geral
                    }
                    pilha_relatorios_aluno.push(estado_antigo)

                    aluno.adicionar_nota(relatorio['nota'])
                    print(f'- Relatório processado para o aluno {aluno.nome}\n- Nova média: {aluno.media_geral:.2f}')

        #* Opcao 4: procurar aluno
        elif opcao == '4':
            try:
                print('\n=== Processo Atual: Procurar por Aluno no Sistema ===')
                matricula = int(input('- Digite a matricula a ser buscada: '))
                aluno = arvore_alunos.buscar(matricula)

                if aluno: #* se o aluno tiver sido encontrado
                    print('-- aluno encontrado!')
                    print(aluno)

            except ValueError:
                print('- Erro. A matricula deve ser um número')

        #* Opcao 5: listar alunos
        elif opcao == '5':
            print('\n=== Processo Atual: Listar Alunos ===')
            arvore_alunos.in_order()

        #* Opcao 6: ver historico
        elif opcao == '6':
            try:
                print('\n=== Processo Atual: Ver Histórico do Aluno ===')
                matricula = int(input('- Digite a matrícula para ver o histórico: '))

                if matricula in pilhas_historico:
                    pilha = pilhas_historico[matricula]

                    if pilha.is_empty():
                        print('-- Nenhuma alteração foi encontrada no histórico do aluno.') 
                    else:
                        print(f'-- Histórico do aluno {matricula} (mais novo para o mais antigo)')
                        no_atual = pilha.topo
                        while no_atual:
                            print(no_atual.dado)
                            no_atual = no_atual.proximo
                else:
                    print(f'- Aluno com matricula {matricula} não encontrado')
            
            except ValueError:
                print('- Erro. A matricula deve ser um número')

        #* Opcao 7: remover aluno
        elif opcao == '7':
            try:
                print('\n=== Processo Atual: Remover Aluno ===')
                matricula = int(input('- Digite a matricula do aluno(a) a ser removido(a): '))
                arvore_alunos.remover(matricula)
            except ValueError:
                print('- Erro. A matricula deve ser um número')

        #* Opcao 8: visualizar arvore
        elif opcao == '8':
            arvore_alunos.display()

        #* Opcao 9: sair
        elif opcao == '9':
            print('\n=== Saindo do Sistema ===')
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()