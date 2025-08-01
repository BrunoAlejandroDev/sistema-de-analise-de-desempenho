# Sistema de Análise de Desempenho e Histórico Escolar (SADHE)

![Python](https://img.shields.io/badge/Python-3.9-blue.svg) ![Status](https://img.shields.io/badge/status-concluído-green.svg) ![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

Um protótipo de software em console para gerenciar o desempenho acadêmico de estudantes, com foco na implementação e aplicação prática de estruturas de dados clássicas como Fila, Pilha e Árvore AVL.

---

### Índice
* [Sobre o Projeto](#sobre-o-projeto)
* [Funcionalidades](#funcionalidades)
* [Arquitetura e Fluxo de Dados](#arquitetura-e-fluxo-de-dados)
* [Estruturas de Dados Implementadas](#estruturas-de-dados-implementadas)
* [Tecnologias e Ferramentas](#tecnologias-e-ferramentas)
* [Como Executar o Projeto](#como-executar-o-projeto)
* [Estrutura de Arquivos](#estrutura-de-arquivos)
* [Futuras Melhorias](#futuras-melhorias)
* [Autor](#autor)

---

### Sobre o Projeto

O SADHE é um sistema em console desenvolvido em Python para gerenciar o desempenho acadêmico de estudantes. O principal objetivo acadêmico é demonstrar a aplicação prática de estruturas de dados clássicas, implementadas do zero, na resolução de um problema do mundo real.

O projeto utiliza Fila, Pilha e, principalmente, uma Árvore AVL auto-balanceável para organizar, processar e consultar informações dos alunos, garantindo um sistema escalável e com performance consistente (O(log n)), mesmo com um grande volume de dados.

---

### Funcionalidades

* 📝 **Cadastro de Alunos:** Inserção de novos alunos no sistema.
* 🗑️ **Remoção de Alunos:** Exclusão de alunos existentes.
* 🚀 **Lançamento de Relatórios:** Adição de novas notas à uma fila de processamento.
* ⚙️ **Processamento em Fila:** Execução ordenada dos relatórios para atualizar os dados dos alunos.
* 🔍 **Busca Eficiente:** Consulta de dados de um aluno específico por matrícula com performance logarítmica.
* 📖 **Histórico de Desempenho:** Visualização de todas as alterações de média de um aluno.
* 📋 **Listagem Ordenada:** Exibição de todos os alunos em ordem crescente de matrícula.
* 🌳 **Visualização da Árvore:** Ferramenta de depuração para exibir a estrutura da Árvore AVL.

---

### Arquitetura e Fluxo de Dados

A arquitetura do sistema é centrada na interação coordenada entre três estruturas de dados principais. O fluxo abaixo descreve o ciclo de vida de uma atualização de desempenho:

![Diagrama de Fluxo de Dados do SADHE](https://i.imgur.com/3n08E41.png)

1.  **Entrada:** Um novo relatório de nota é submetido pelo usuário.
2.  **Enfileiramento:** O relatório entra em uma **Fila de Processamento**, garantindo que a ordem de chegada (FIFO) seja respeitada.
3.  **Processamento:** O sistema retira o primeiro relatório da fila para processá-lo.
4.  **Busca na Árvore:** O aluno correspondente é buscado na **Árvore AVL** (banco de dados em memória) em tempo $O(\log n)$.
5.  **Backup na Pilha:** O estado de desempenho antigo do aluno é salvo em sua **Pilha de Histórico** individual (LIFO).
6.  **Atualização:** Os dados do aluno são finalmente atualizados no nó da Árvore AVL.

---

### Estruturas de Dados Implementadas

* **Árvore AVL (AVL Tree):**
    * **Papel:** Estrutura de armazenamento principal.
    * **Justificativa:** Escolhida sobre uma Árvore de Busca Binária comum para garantir performance de $O(\log n)$ em todas as operações (busca, inserção, remoção), evitando o pior caso de $O(n)$ através do mecanismo de auto-balanceamento.

* **Fila (Queue):**
    * **Papel:** Gerenciador da esteira de processamento de relatórios.
    * **Justificativa:** O comportamento FIFO (First-In, First-Out) é ideal para garantir que os relatórios sejam processados de forma justa e na ordem correta, desacoplando a submissão do processamento.

* **Pilha (Stack):**
    * **Papel:** Armazenamento do histórico de alterações de cada aluno.
    * **Justificativa:** O comportamento LIFO (Last-In, First-Out) é o mais intuitivo para uma funcionalidade de "ver histórico", permitindo que o usuário veja sempre as alterações mais recentes primeiro.

---

### Tecnologias e Ferramentas

* **Linguagem:** Python 3.9
* **Controle de Versão:** Git / GitHub
* **Gerenciamento de Projeto:** Trello (Metodologia baseada em Kanban)
* **Empacotamento:** PyInstaller (para a criação do arquivo executável)

---

### Como Executar o Projeto

Existem duas maneiras de executar o sistema:

**Opção 1: Usando o Executável (Recomendado)**
1.  Baixe o arquivo `SADHE.exe` (ou `main.exe`) da pasta `dist/` do projeto.
2.  Coloque-o em uma pasta de sua preferência.
3.  Dê um duplo clique para executar. Um terminal será aberto com o menu interativo do sistema.

**Opção 2: A partir do Código-Fonte**
1.  Garanta que você tem o **Python 3** instalado em sua máquina.
2.  Clone este repositório: `git clone https://github.com/seu-usuario/seu-repositorio.git`
3.  Navegue até a pasta do projeto: `cd seu-repositorio`
4.  Execute o arquivo principal: `python main.py`

---

### Estrutura de Arquivos
```
SADHE/
├── main.py             # Ponto de entrada da aplicação e menu interativo
├── aluno.py            # Definição da classe Aluno
├── arvore_avl.py       # Implementação da classe ArvoreAVL
├── avl_node.py         # Definição da classe AvlNode
├── fila.py             # Implementação da classe Fila
├── pilha.py            # Implementação da classe Pilha
├── node.py             # Definição da classe Node genérica para Fila/Pilha
└── README.md           # Este arquivo
```

---

### Futuras Melhorias

O projeto foi construído de forma modular para permitir futuras expansões:

* **Persistência de Dados:** Salvar o estado da árvore em um arquivo (JSON) para que os dados não sejam perdidos ao fechar o sistema.
* **Interface Gráfica ou Web:** Substituir a interface de console por uma interface construída com o framework web Django.
* **Sistema de Sugestões de Estudo:** Expandir a funcionalidade de "conteúdos com dificuldade" para sugerir materiais de estudo.
* **Exportação de Relatórios:** Gerar arquivos `.txt` ou `.pdf` com o boletim completo de um aluno.

---

### 🛠️ Autor

**Bruno Pimentel**  
Desenvolvedor Back-end com foco em Desenvolvimento Web, Ciência de Dados, Automações e Machine Learning.  

- GitHub: [@BrunoAlejandroDev](https://github.com/BrunoAlejandroDev)
- LinkedIn: [Bruno Pimentel](https://www.linkedin.com/in/seu-perfil)
