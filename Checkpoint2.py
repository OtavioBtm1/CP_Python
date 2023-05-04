# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132
# cria um dicionário vazio para representar o estoque


######################### CADASTRO DE CLIENTE# #############################
pos=["sim", "Sim", "S", "s", "Ss", "ss"]

print("Seja bem-vindo à Vinheria Agnello!")
dec = None
while dec is None:
    dec=input("Você deseja realizar uma compra? Se sim, vamos para o cadastro!")
    if dec in pos:
        nome = input("Digite seu primeiro nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        idade = int(input("Digite sua idade: "))

        print("\nAgora vamos para o cadastro de endereço!")

        rua = None 
        while rua is None:
            rua = input("Digite o nome da sua rua: ")

        bairro = None
        while bairro is None:
            bairro = input("Digite o bairro: ")

        num = None
        while num is None:
            num = input("Digite o número da casa: ")

        cep = None
        cep_str = input("Digite o CEP: ")
        try:
            cep = int(cep_str)
        except ValueError:
                print("Por favor, digite um CEP válido.")

        comp = None
        while comp is None:
        
            comp = input("Digite o complemento (opcional): ") or None

##########################SISTEMA DE ESTOQUE E COMPRA#################
estoque = {"vinho tinto": 10, "vinho branco": 5, "espumante": 8}  # Dicionário para controle de estoque
precos = {"vinho tinto": 50.0, "vinho branco": 40.0, "espumante": 70.0}  # Dicionário para controle de preços

print("Seja bem-vindo à Vinheria Agnello!")
print("Estes são os produtos disponíveis e seus respectivos preços:")
for produto, preco in precos.items():
    print(f"- {produto.capitalize()}: R$ {preco:.2f}")

while True:
    # Loop para receber as compras do usuário
    compra = input("\nDigite o produto que deseja comprar ou 'sair' para encerrar: ").lower()

    if compra == "sair":
        print("\nObrigado por comprar na Vinheria Agnello!")
        break

    # Verifica se o produto está disponível no estoque
    if compra not in estoque:
        print("Desculpe, produto não disponível.")
        continue

    quantidade = int(input(f"Digite a quantidade de {compra.capitalize()} que deseja comprar: "))
    if quantidade > estoque[compra]:
        print(f"Desculpe, não temos {quantidade} unidades de {compra.capitalize()} em estoque.")
        continue

    # Calcula o valor total da compra
    valor_total = quantidade * precos[compra]
    print(f"O valor total da sua compra de {quantidade} unidades de {compra.capitalize()} é de R$ {valor_total:.2f}")

    # Atualiza o estoque
    estoque[compra] -= quantidade
##########################SISTEMA DE ESTOQUE E COMPRA#################

else:
        print("Obrigado, tenha um bom dia!")
######################### CADASTRO DE CLIENTE# #############################


