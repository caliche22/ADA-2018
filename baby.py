from sys import stdin
import operator
##Carlos Saul Arboleda ADA Tarea2 Babylon 
## Se hace uso de la libreria operator para poder comparar dos cosas 
## Se utiliza los codigos de lis para encontrar la longitud de la subsecuencia incrementativa del profesor vista en clase por memorizacion
## Se discutio la idea del operator con Juan Sebastian Rivera y Maria Paula 

bloques = [] ## lista vacia para guardar las permutaciones

def PermutacionesBase(x,y,z): ## permutaciones se hace las combinaciones a mano 
	global bloques
	bloques.append([x,z,y])
	bloques.append([x,y,z])
	bloques.append([y,z,x])
	bloques.append([y,x,z])
	bloques.append([z,x,y])
	bloques.append([z,y,x])

def aux_memoization(bloques,n,memo): ## codigo del profesor
  ans = memo[n]
  if ans==None:
    ans = 0
    for i in range(n):
      if bloques[i][0]>bloques[n][0] and bloques[i][1]>bloques[n][1] : #Modificado aqui para verificar tanto X como Y, que ambas deben ser estrictamente mayores que el siguiente
        ans = max(ans,aux_memoization(bloques,i,memo))
    ans += bloques[n][2] #Modificado aqui para no sumar 1 si no modificar el Z
    memo[n] = ans
  return ans

def lis_memoization(bloques): ## codigo del profesor
  N = len(bloques)
  ans = 0
  if N!=0:
    memo = [ None for i in range(N) ]
    for n in range(N):
      ans = max(ans,aux_memoization(bloques,n,memo))
  return ans


def main():
	global bloques,x,y,z
	line = 1
	case = 1
	while int(line) != 0: ## condicion parada 
		contador = 0
		line = int(stdin.readline().strip())
		while contador < line: ## condicion de lectura
			j = stdin.readline().strip().split()
			x,y,z = [int(k) for k in j] ## dimensiones 
			PermutacionesBase(x,y,z)## posibilidades
			contador = contador + 1
		bloques.sort(key = operator.itemgetter(0, 1)) # se necesitaba el operator toco importarloOrdenar la lista aqui para enviarla al LIS, se ordena de mayor a menor primero por X y luego por Y
		bloques.reverse() ## mayor a menor 
		if int(line) != 0:
			#print("Case {}: maximum height = {}".format(case,lis_memoization(bloques))) como cosa rara no me funciona asi 
			case=str(case)
			print("Case "+case+":","maximum height =",lis_memoization(bloques))
			case = int(case) + 1
			bloques = []## vacio la lista para meter las nuevas permutaciones limpio


main()

