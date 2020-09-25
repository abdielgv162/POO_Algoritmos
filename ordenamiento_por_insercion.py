import random

def ordenamiento_por_insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual

    return lista


def ordenamiento_por_insercion_2(lis):
    ordenada = []
    ordenada.append(lista[0])
    for i in range(1, len(lista)):
        indice_actual = lista[i]
        while indice_actual > 0 and indice_actual < lista[i-1]:
            indice_actual , list[i-1] = list[i-1], indice_actual
            indice_actual -= 1
            
    return lista




if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(f'Lista original: {lista} \n')
    
    lista_ordenada_1 = ordenamiento_por_insercion(lista)
    print(f'Lista ordenada por el primer algoritmo: {lista_ordenada_1} \n')

    lista_ordenada_2 = ordenamiento_por_insercion_2(lista)
    print(f'Lista ordenada por el segundo algoritmo: {lista_ordenada_2} \n')


 
 
