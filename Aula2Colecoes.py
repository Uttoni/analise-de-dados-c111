#tuplas - coleção mais simples do python
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
