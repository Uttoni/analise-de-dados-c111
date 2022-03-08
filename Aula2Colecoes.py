#tuplas - coleção mais simples do python - imutavel---------------------------------------------------------------------
people = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(people[1])
# slicing de dados
print(people[0:2])
print(people[1:])
print(people[1], people[3])
print('tamanho:', len(people))

ddiBrasil = (55, "Brasil")
ddiRussia = (7, "Rússia")
ddiPeru = (51, "Alemanha")
#ddiPeru[1] = "Peru" # não é possível alterar uma tupla selecionando a posição do dado como numa lista
print(ddiBrasil, ddiRussia, ddiPeru)
print("ddi brasil:", ddiBrasil[0])
print(len(ddiBrasil))

# tuplas podem ter mais de 2 dados
paises = ('Brasil', 'EUA', 'China', 'Holanda')
print(paises)
print('indice negativo:', paises[-2])
for pais in paises:
    print(pais)

#listas - mutavel ------------------------------------------------------------------------------------------------------
frutas = ['apple', 'banana', 'pear']
#add elementos
frutas.append('grapes')
frutas.insert(1, 'pineapple')
print(frutas)

#deletar elementos
frutas.pop(2)
frutas.remove('pineapple')

#alterar elementos
frutas[2] = 'peach'
print(frutas)

#conjuntos(sets) - não aceita dados repetidos --------------------------------------------------------------------------
langs = {'english', 'portuguese', 'french', 'french'}

# add dados
langs.add('german')
langs.update(frutas)  # adiciona uma coleção dentro do set
langs.remove('portuguese')
print(langs)

# dicionario - usa indices customizaveis -------------------------------------------------------------------------------
estados = {'MG':'Minas Gerais', 'AL':'Alagoas', 'TO':'Tocantins'}
pessoa = {'nome': 'Uttoni', 'idade': 21}

pessoa['cidade'] = 'Borda da Mata' # adiciona porque não tem
pessoa['idade'] = 22 # altera o valor porque tem o índice idade
pessoa.pop('nome') # remove o valor passado o índice

print(estados)
print(pessoa)

#Casting - conversões
frutasSet = set(frutas)
langsList = list(langs)
frutasTuple = tuple(frutas)

