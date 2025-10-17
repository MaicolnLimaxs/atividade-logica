# Vetor com o estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender_produto(estoque, produto, quantidade):
    if estoque[produto - 1] >= quantidade:
        estoque[produto - 1] -= quantidade
        print(f"Venda realizada: {quantidade} unidades do produto {produto}")
    else:
        print(f"Estoque insuficiente para o produto {produto}!")

# Função para adicionar produtos ao estoque
def adicionar_produto(estoque, produto, quantidade):
    estoque[produto - 1] += quantidade
    print(f"Foram adicionadas {quantidade} unidades ao produto {produto}")

# Função para exibir o estoque atual
def exibir_estoque(estoque):
    print("\nEstoque Atualizado:")
    for i in range(len(estoque)):
        print(f"Produto {i+1}: {estoque[i]} unidades")

# --- Operações solicitadas ---
vender_produto(estoque, 1, 3)  # Vender 3 do produto 1
vender_produto(estoque, 4, 2)  # Vender 2 do produto 4
adicionar_produto(estoque, 5, 10)  # Adicionar 10 ao produto 5

# Exibir resultado final
exibir_estoque(estoque)
