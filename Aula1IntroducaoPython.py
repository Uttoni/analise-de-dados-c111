'''
print("k", 3+5)
answer = input('Mano que preguiça, pqp. Como cễ tá?')
print(answer)
idade = int(input("Quantos anos tu tem mesmo?"))
print(idade, type(idade))
print(f'vc tem {idade} anos e já tá {answer}')

#multiplicação de string
print("sono" * 20)
'''

# Exercicio 1

nome = input("Entre com seu nome completo: \n")
print('Nome completo: ', nome)
print('Maiúsculas: ', nome.upper())
print('Minúsculas: ', nome.lower())
print('Tamanho: ', len(nome))
print('Trocado', nome.replace('Brandani', 'do Inatel'))

#Exercicio 2

numero = int(input("Escolha um número: "))
inicio = int(input("Escolha o número de inicio da tabuada: "))
fim = int(input("Escolha o número de fim da tabuada: "))

while inicio <= fim:
    print(f"{numero}x{inicio} = {numero*inicio}")
    inicio += 1

#Exercicio 3
sexo = 'nada'
while(sexo != 'M' and sexo != 'F'):
    sexo = input('Entre com M para homem ou F para mulher: ')









