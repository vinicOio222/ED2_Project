class HashTable:
    def __init__(self, size):
        """ Inicializa a tabela hash com um tamanho fixo e a preenche com None """
        self.size = size
        self.table = [None] * size
    
    def hash_default(self, k):
        """ 
        Função hash primária que determina a posição base onde a chave deve ser inserida.
        Retorna o índice calculado como k % tamanho da tabela. 
        """
        return k % self.size
    
    def hash_alternative(self, k):
        """ 
        Função hash secundária usada para dispersão dupla. 
        Retorna um deslocamento baseado em 1 + (k % (m - 1)), garantindo um salto maior 
        e ajudando a distribuir melhor os elementos. 
        """
        return 1 + (k % (self.size - 1))
    
    def insert_linear(self, key):
        """ 
        Inserção utilizando tentativa linear. 
        Se houver colisão, a próxima posição disponível é buscada de forma sequencial (i + 1). 
        """
        index = self.hash_default(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            i += 1  # Incrementa para verificar a próxima posição
        self.table[(index + i) % self.size] = key
    
    def insert_quadratic(self, key, c1, c2):
        """ 
        Inserção utilizando tentativa quadrática. 
        Se houver colisão, o deslocamento cresce quadraticamente (c1 * i + c2 * i²). 
        """
        index = self.hash_default(key)
        i = 0
        while self.table[(index + c1 * i + c2 * i**2) % self.size] is not None:
            i += 1  # Incrementa para tentar uma nova posição
        self.table[(index + c1 * i + c2 * i**2) % self.size] = key
    
    def insert_double_hashing(self, key):
        """ 
        Inserção utilizando dispersão dupla. 
        Se houver colisão, um novo deslocamento é calculado com uma segunda função hash. 
        """
        index = self.hash_default(key)
        step = self.hash_alternative(key)
        i = 0
        while self.table[(index + i * step) % self.size] is not None:
            i += 1  # Incrementa para testar uma nova posição
        self.table[(index + i * step) % self.size] = key
    
    def display(self):
        """ Exibe a tabela hash mostrando o índice e o valor armazenado """
        for i, key in enumerate(self.table):
            print(f'Index {i}: {key}')


if __name__ == '__main__':
    # Definição do tamanho da tabela e conjunto de chaves
    table_size = 11
    keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]

    # Inserção usando tentativa linear
    print("Tentativa Linear:")
    linear_table = HashTable(table_size)
    for key in keys:
        linear_table.insert_linear(key)
    linear_table.display()
    print("\n")

    # Inserção usando tentativa quadrática
    print("Tentativa Quadrática:")
    quadratic_table = HashTable(table_size)
    for key in keys:
        quadratic_table.insert_quadratic(key, 1, 3)
    quadratic_table.display()
    print("\n")

    # Inserção usando dispersão dupla
    print("Dispersão Dupla:")
    double_hash_table = HashTable(table_size)
    for key in keys:
        double_hash_table.insert_double_hashing(key)
    double_hash_table.display()
