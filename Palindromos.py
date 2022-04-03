

from pickle import TRUE
from sqlalchemy import false, true
def palindromo(palabra):
    palabra=palabra.replace(' ','') #Primero se quitan los espacios vacíos: Luz Azul --> Luzazul
    palabra=palabra.lower() #ahora estaría luzazul
    palabra_invertida=palabra[::-1] #Vamos desde el final hasta el principio de 1 en 1
    if palabra==palabra_invertida: # Si es palíndromo me va a dar true
        return true
    else:
        return false


def run():
    palabra=input('Escribe una palabra: ')
    es_palindromo=palindromo(palabra)
    if es_palindromo==true: #Si es true nos va a dar que sí lo es
        print('Es palíndromo')
    else:
        print('No es palíndromo')


#Entry point: es una buena práctica. 
if __name__=='__main__':
    run()


