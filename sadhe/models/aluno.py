class Aluno:
    '''
    Sobre: Representa um aluno no sistema e suas informações.
    Métodos: 
        adicionar_nota
        adicionar_falta
        adicionar_dificuldade
    '''
    #* Construtor da classe
    def __init__(self, matricula: int, nome: str):
        if not isinstance(matricula, int):
            raise TypeError('Erro: Matricula deve ser um numero inteiro')
        if not nome or not isinstance(nome, str):
            raise TypeError('Erro: Nome nao deve ser um texto vazio.')
        
        self.matricula = matricula
        self.nome = nome
        self.notas = []
        self.faltas = 0
        self.conteudos_com_dificuldade = []
        self.media_geral = 0.0
        
    #* Metodo para adicionar uma nova nota
    def adicionar_nota(self, nota: float):
        
        #* verificar se a nota é um valor numerico
        if not isinstance(nota, (int, float)): 
            raise ValueError('Nota deve ser um valor numerico.')
        
        #* se nota for valor numerico, adicionar nova nota na lista de notas
        self.notas.append(nota)
        self._calcular_media()
        
    #* Metodo para calcular media do aluno
    def _calcular_media(self):
        
        #* verificar se a lista de notas está vazia, caso sim retorna 0
        if not self.notas:
            self.media_geral = 0.0
        else: #* se a lista nao estiver vazia, calcular media
            self.media_geral = sum(self.notas) / len(self.notas)
            
    #* Metodo para adicionar uma ou mais faltas ao aluno
    def adicionar_falta(self, quantidade: int = 1):
        '''
        Adiciona uma ou mais faltas no valor de faltas do aluno
        '''
        self.faltas += quantidade
        
    #* Metodo para adicionar um conteúdo de dificuldade
    def adicionar_dificuldade(self, conteudo:str):
        '''
        Metodo para adicionar um conteudo à lista de conteudos com dificuldade do aluno
        '''
        #* Verificar se o conteudo não existe na lista antes de adicionar
        if conteudo not in self.conteudos_com_dificuldade:
            self.conteudos_com_dificuldade.append(conteudo)
     
    def __str__(self):
        '''
        Retorna uma representação em string do objeto Aluno, para facilitar a impressão.
        '''
        return f"Matrícula: {self.matricula} | Nome: {self.nome.capitalize()} | Média: {self.media_geral:.2f} | Faltas: {self.faltas}"