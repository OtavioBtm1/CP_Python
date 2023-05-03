# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944
# Eduardo Fedeli 550132
######################### CADASTRO DE CLIENTE# #############################
print("Seja bem-vindo à Vinheria Agnello!")
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
######################### CADASTRO DE CLIENTE# #############################


