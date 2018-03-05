#Parcial 1
#ADA Carlos Saul Arboleda
#Palindrome
 
#Resolucion po programacion dinamica, en sintesis se basa en recorrer el arreglo con un indice i
#buscando palindromes desde el inicio hasta el indice dando, se crea un arreglo ans que tendra
#el numero de particiones minimas para el sub arreglo [j...i] donde se ira guardando a medida 
#se recorre el arreglo, el peor de los casos el unico palindrome sera el caracter en la 
#posicion i el cual se le sumara el corte anterior ans[i] = 1 + ultimo corte hecho
# de otra manera se tomara el minimo palindrome encontrado y para ans[i] = el corte necesario para el inicio del palindrome +1 que sera dado el resto de la cadena.

from sys import stdin

def esPalindrome(line): ## funcion es palindrome si o no True o False
    ans = True
    n = len(line)
    for i in range(0,n):
        if line[i] != line[n -1 -i]:
            ans = False
            break ## lo hago salirse de alli
    return ans
     
def solve(line,n):
    tab = [float("inf")] * (n+1) ## lleno tab para comenzar
    tab[0] = 0 #primera pos
    for i in range(1,n+1): ## rango del arreglo
        for j in range(0,i):
            if esPalindrome(line[j:i]): ## slice de la lista line para preguntar si esa parte es palindrome o no
                tab[i] = min(tab[i],1+tab[j]) ## despues el minimo entre los dos anterior y presente
    return tab[n]
     
def main():
    global dataIn,line
    dataIn = stdin
    numCases = int(dataIn.readline())
    for i in range(0,numCases):
        line = dataIn.readline()
        n = len(line)
        if(i == numCases -1):
            print(solve(line,n)-1)
        else:
            print(solve(line,n-1))
main()
 
#Fuentes: https://www.youtube.com/watch?v=lDYIvtBVmgo se uso de guia el video tutorial..