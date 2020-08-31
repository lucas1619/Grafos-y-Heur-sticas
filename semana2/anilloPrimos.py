def isPrime(n) : 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6
    return True

def permuta():
    respuesta = []
    respuestas = []
    ene = int(input('Ingresa N:'))
    def bt(n):
        for i in range(1,n+1):
            if len(respuesta) == 0:
                respuesta.append(i)
                bt(n)
                respuesta.pop(-1)
            else:
                if respuesta.count(i) == 1:
                    continue
                else:
                    suma = respuesta[-1] + i
                    if isPrime(suma):
                        respuesta.append(i)
                        if len(respuesta) == n:
                            suma2 = respuesta[-1] + respuesta[0]
                            if isPrime(suma2):
                                respuestas.append(respuesta.copy())
                                respuesta.pop(-1)
                                return
                            else:
                                respuesta.pop(-1)
                                continue
                        else:    
                            bt(n)
                            respuesta.pop(-1)
                    else:
                        continue                
    bt(ene)
    if len(respuestas) == 0:
        print(f'No hay respuestas para n = {ene}')
        return
    for i, ans in enumerate(respuestas):
        print(f'{ans} num {i + 1}')

if __name__ == "__main__":
    permuta() 