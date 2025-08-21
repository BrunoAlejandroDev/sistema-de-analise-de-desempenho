
#* Importacoes
import json

#* Funcao para salvar os arquivos
def salvar_arquivo(arvore, pilha_historico, nome_arquivo):
    try:
        print('Processo Atual: Salvar Arquivos')
        
        #* Verificar se a arvore e o historico estao vazios
        if arvore.raiz is None and not pilha_historico:
            print('-- Não existem dados para salvar. A árvore está vazia.')
            return
        
        #* Traduzir a arvore para um dicionario
        arvore_serializada = arvore.serializar()
        
        #* Traduzir o dicionario de pilhas para um dict de listas
        historico_serializado = {}
        for matricula, pilha in pilha_historico.items():
            historico_serializado[str(matricula)] = pilha.to_list()

        #* Juntas os dados em um unico dicionario
        dados_completos = {
            'arvore' : arvore_serializada,
            'pilha_historico' : historico_serializado
        }

        #* Escrever os dados no arquivo JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as file:
            json.dump(dados_completos, file, indent=4, ensure_ascii=False)
        
        print(f'-- Dados salvos com sucesso em {nome_arquivo}.')
    
    except Exception as e:
        print(f'-- Ocorreu um erro ao salvar os dados.\n{e}')
