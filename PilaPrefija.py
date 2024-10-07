def evaluar_prefija(expresion):
    pila = []
    
    for simbolo in expresion[::-1]:
        if simbolo.isdigit(): 
            pila.append(int(simbolo))
        else:

            a = pila.pop()
            b = pila.pop()
            
            if simbolo == '+':
                resultado = a + b
            elif simbolo == '-':
                resultado = a - b
            elif simbolo == '*':
                resultado = a * b
            elif simbolo == '/':
                resultado = a / b
            
            pila.append(resultado)
    
    return pila.pop()  

expresion = "+9*26"
resultado = evaluar_prefija(expresion)
print(f"El resultado de la expresión prefija {expresion} es: {resultado}")
