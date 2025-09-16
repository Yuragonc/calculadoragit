def sumar(a: float, b: float) -> float:
    #Suma dos números.
    return a + b

def restar (a: float, b: float) -> float:
    #Resta el segundo número al primero.
    return a - b

def multiplicar(a: float, b: float) -> float:
    #Multiplica dos números.
    return a * b

def dividir(a: float, b: float) -> float:
   #Divide el primer número por el segundo.
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print(sumar(2, 2))          
    print(restar(7, 1))         
    print(multiplicar(8, 2))    
    print(dividir(12, 2))       

