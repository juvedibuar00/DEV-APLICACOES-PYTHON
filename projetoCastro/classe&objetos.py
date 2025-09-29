

def adicionar_produto(lista, produto):
    """
    Adiciona um produto a uma lista.
    """
    lista.append(produto)

    """
lista representa o container onde os produtos serão armazenados. produto é o item que queremos adicionar.
 append() é um método de listas que insere um item no final.
    """


produtos = []
produto = {"nome": "Caneta", "preco": 2.5, "quantidade": 10}
adicionar_produto(produtos, produto)
print(produtos)


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(f"{self.nome} - {self.preco} - {self.quantidade}")


        """
        __init__ é o construtor, executado ao criar um objeto.

self referencia o objeto em si.

exibir() é um método que mostra os dados do produto.
        """


produto1 = Produto("Caneta", 2.5, 10)
produto1.exibir()  # Saída: Caneta - 2.5 - 10





# Persistência de Dados com JSON


import json

produtos = [produto1]

# Salvar no arquivo
with open("produtos.json", "w") as f:
    json.dump([p.__dict__ for p in produtos], f)

# Ler do arquivo
with open("produtos.json", "r") as f:
    produtos_carregados = json.load(f)

print(produtos_carregados)


produto1 = Produto("Caneta", 2.5, 10)
produto2 = Produto("Caderno", 15.0, 5)
produto3 = Produto("Borracha", 1.0, 20)
produto4 = Produto("Lápis", 1.5, 15)
produto5 = Produto("Apontador", 3.0, 8)
