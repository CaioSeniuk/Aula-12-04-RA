lista = [2,4,7,2,3,3,1,0,2,6]
maior = []
for i in lista:
    maior.append(lista.count(i))
maisrepetido = lista[maior.index(max(maior))]
print(f"\nO número mais repetido na lista foi o: {maisrepetido}\n")