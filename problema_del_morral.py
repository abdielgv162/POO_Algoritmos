#Zero-one solucionado con recursividad 

def morral(tamano_morral, pesos, valores, n):
    if n == 0 or tamano_morral == 0:
        return 0
        
    if pesos[n-1] > tamano_morral :
        return morral(tamano_morral, pesos, valores, n-1)
    
    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1),#Lo escojo
                morral(tamano_morral, pesos, valores, n-1))#No lo escojo

if __name__ == '__main__':
    valores = [60,100,120]
    pesos = [10,20,30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado) 