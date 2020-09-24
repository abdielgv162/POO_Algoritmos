import random

def busqueda_lineal(lista, objetivo,contador1=0):
    match = False

    for elemento in lista:
        contador1 += 1
        if elemento == objetivo:
            match = True
            break
    return (match,contador1)


def busqueda_binaria(lista, comienzo, final, objetivo,contador2=0):
    contador2 += 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    if comienzo > final:
        return (False,contador2)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        
        return (True,contador2)

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo,contador2)
    else: 
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo,contador2)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,10000) for i in range(tamano_de_lista)])
    #La funcion sorted() ordena la lista.

    (encontrado_lineal, contador1) = busqueda_lineal(lista, objetivo)
    (encontrado_binario, contador2) = busqueda_binaria(lista, 0, len(lista), objetivo)


    print(f'El elemento {objetivo} {"esta" if encontrado_binario and encontrado_lineal else "no esta"} en la lista') 
    print(f'Cantidad de iteraciones para la busqueda lineal: {contador1} ')
    print(f'Cantidad de iteraciones para la busqueda binaria: {contador2} ')
