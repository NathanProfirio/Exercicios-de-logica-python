estoque = {
        'nome':["tv", "bola"],
        'preço':[1500.85, 4.78],
        'quantidade':[8, 20],
    }

def limpar_terminal():
    print("\n"*50)

def mostra_produto(posicao):
    return print(f"{"="*50}\nProduto: {estoque["nome"][posicao]} \nPreço: R${estoque["preço"][posicao]:.2f} \nQuantidade: {estoque["quantidade"][posicao]}\n{"="*50}")


def cadrastro_produtos():
    limpar_terminal()
    print("Para cadrasta um novo produto digite o Nome, Preço e a Quantidade que vai entra no estoque do produto")
    nome = input("nome do produto: ")
    if nome in estoque["nome"]:
        limpar_terminal()
        print(f"O produto {nome} ja esta cadrastrado")
    else:
        preco = float(input("Qual o preço do produto: "))
        quantidade = int(input("Qual o estoque do produto: "))
        estoque['nome'].append(nome)
        estoque['preço'].append(preco)
        estoque['quantidade'].append(quantidade)
        posicao = len(estoque["nome"]) - 1
        limpar_terminal()
        print("O produto abaixo foi cadrastado no estoque")
        mostra_produto(posicao) 

def remover_produto():
    limpar_terminal()
    produto = input("Qual o nome do produto que você desseja remover: ")
    if produto in estoque["nome"]:
        posicao = estoque["nome"].index(produto)
        del estoque["nome"][posicao]
        del estoque["preço"][posicao]
        del estoque["quantidade"][posicao]
        limpar_terminal()
        print(f"O produto {produto} foi removido do estoque")
    else:
        limpar_terminal()
        print(f"o produto que você digitou {produto} não existe")

def lista_produtos():
    limpar_terminal()
    for i in range(len(estoque["nome"])):
        print("="*50)
        print(f"Produto: {estoque['nome'][i]} \nPreço: R${estoque['preço'][i]:.2f} \nQuantidade: {estoque['quantidade'][i]}")
        print("="*50)

def atualizar_produto():
    produto = input("Qual o nome do produto que você que altera: ")
    if produto in estoque["nome"]:
        posicao = estoque["nome"].index(produto)
        limpar_terminal()
        print("Qual campo você gostaria de altera")
        print("[1] Nome") 
        print("[2] Preço")
        print("[3] Quantidade")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alteracao = input("Qual o novo nome do produto: ")
            nome_antigo = estoque["nome"][posicao]
            estoque["nome"][posicao] = alteracao
            limpar_terminal()
            print(f"O nome do produto foi alterado de {nome_antigo} para {estoque["nome"][posicao]}")
            mostra_produto(posicao)
        elif opcao == "2":
            alteracao = float(input("Qual o novo preço do produto: "))
            preco_antigo = estoque["preço"][posicao]
            estoque["preço"][posicao] = alteracao
            limpar_terminal()
            print(f"O preço do produto {estoque["nome"][posicao]} foi alterado de R${preco_antigo:.2f} para R${estoque["preço"][posicao]:.2f}")
            mostra_produto(posicao)
        elif opcao == "3":
            alteracao = int(input("Qual a nova quantidade do produto: "))
            estoque_antigo = estoque["quantidade"][posicao]
            estoque["quantidade"][posicao] = alteracao
            limpar_terminal()
            print(f"A quantidade do estoque do produto {estoque["nome"][posicao]} foi alterado de {estoque_antigo} para {estoque["quantidade"][posicao]}")
            mostra_produto(posicao)
        else:
            print("Opção invalida")

while True:

    print(f"{"="*10} Escolha uma das opções abaixo {"="*10}")
    print("""[1] Adicionar um novo produto ao estoque.
[2] Remover um produto do estoque por nome.
[3] Listar todos os produtos em estoque.
[4] Atualizar informações de um produto existente.
[5] Sair do programa.""")
    opcao = input("Sua escolha: ")

    if opcao == "1":
        cadrastro_produtos()

    elif opcao == "2":
        remover_produto()

    elif opcao == "3":
        lista_produtos()

    elif opcao == "4":
        atualizar_produto()
        
    elif opcao == "5":
        limpar_terminal()        
        print(f"{"="*30} \nPrograma Finalizado \n{"="*30}")
        break
    
    else:
        limpar_terminal()
        print(f"{"="*50} \nEscolha uma opção valida \n{"="*50}")