import csv
import json
# =========================================================
# Aula 1 – Funções, Classes e Persistência em JSON
# =========================================================

# ---------------------------------------------------------
# 1. Funções e Parâmetros
# ---------------------------------------------------------
# Definição:
# Função: bloco de código reutilizável que realiza uma tarefa específica
# Parâmetros: valores passados para a função para que ela funcione de forma genérica

def adicionar_produto(lista, produto):
    """
    Adiciona um produto a uma lista.
    Parametro lista: lista onde os produtos são armazenados
    Param produto: produto a ser adicionado
    """
    # adiciona o produto ao final da lista
    lista.append(produto)

# 
produtos = []  # lista vazia para armazenar produtos
produto_exemplo = {"nome": "Caneta", "preco": 2.5, "quantidade": 10}

# chama a função para adicionar o produto
adicionar_produto(produtos, produto_exemplo)

# Impressão da listar e conferência dos produtos
print("Lista após adicionar produto de exemplo:")
print(produtos)
print("-"*50)

# ---------------------------------------------------------
# 2. Classes e Objetos
# ---------------------------------------------------------
# Definição:
# Classe: molde que define atributos e métodos de um tipo de objeto
# Objeto: instância concreta da classe, que armazena dados reais e executa métodos

class Produto:
    def __init__(self, nome, preco, quantidade):
        """
        Construtor da classe Produto
        """
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        """
        Exibe informações do produto
        """
        print(f"{self.nome} - {self.preco} - {self.quantidade}")

# Criando objetos
produto1 = Produto("Caneta", 2.5, 10)
produto2 = Produto("Caderno", 15.0, 5)
produto3 = Produto("Borracha", 1.0, 20)
produto4 = Produto("Lapis", 1.5, 15)
produto5 = Produto("Apontador", 3.0, 8)
produto6 = Produto("Pas. Slides", 25.5, 4)
produto7 = Produto("Mochila", 120.0, 3)


# Usando o método exibir()
print("Exibindo produtos criados:")
produto1.exibir()
produto2.exibir()
produto3.exibir()
produto4.exibir()
produto5.exibir()
produto6.exibir()
produto7.exibir()
print("-"*50)

# ---------------------------------------------------------
# 3. Adicionar objetos a uma lista usando a função
# ---------------------------------------------------------
lista_produtos = []
adicionar_produto(lista_produtos, produto1)
adicionar_produto(lista_produtos, produto2)
adicionar_produto(lista_produtos, produto3)
adicionar_produto(lista_produtos, produto4)
adicionar_produto(lista_produtos, produto5)
adicionar_produto(lista_produtos, produto6)
adicionar_produto(lista_produtos, produto7)

print("Lista de objetos adicionados:")
for p in lista_produtos:
    p.exibir()
print("-"*50)

# ---------------------------------------------------------
# 4. Persistência de Dados com JSON
# ---------------------------------------------------------
# Definição:
# JSON: formato leve para armazenar e transportar dados estruturados
# Permite salvar objetos em arquivo e carregá-los posteriormente



# Salvar lista de objetos no arquivo JSON
with open("produtos.json", "w") as f:
    # converte cada objeto em dicionário usando __dict__
    json.dump([p.__dict__ for p in lista_produtos], f)

print("Produtos salvos em 'produtos.json'.")

# Ler dados do arquivo JSON
with open("produtos.json", "r") as f:
    produtos_carregados = json.load(f)

print("Produtos carregados do arquivo JSON:")
print(produtos_carregados)
print("-"*50)

# ---------------------------------------------------------
# Fim da aula 1
# Benefício:
# Criamos funções, objetos, adicionamos em listas e salvamos/carregamos usando JSON
# Prática essencial para sistemas reais
# ---------------------------------------------------------



# Abrir o arquivo JSON
with open("produtos.json", "r") as f:
    produtos = json.load(f)

# Mostrar título da tabela
print(f"{'NOME':<15} {'PREÇO':<10} {'QUANTIDADE':<10}")
print("-"*35)

# Percorrer produtos e imprimir cada um
for p in produtos:
    nome = p.get("nome", "")
    preco = p.get("preco", 0)
    quantidade = p.get("quantidade", 0)
    print(f"{nome:<15} {preco:<10} {quantidade:<10}")





# --- Salvando em CSV (usando dicts do JSON) ---
with open("produtos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Preço", "Quantidade"])
    for p in produtos_carregados:
        writer.writerow([p["nome"], p["preco"], p["quantidade"]])