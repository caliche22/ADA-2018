from sys import stdin
from heapq import heappop,heappush
delta = [(-1,0),(0,-1),(0,1),(1,0)] ## derecha izquierda arriba abajo fronteras
INF = float('inf')
#Carlos Saul Arboleda 
# 0061863
#Codigo sssp del profesor Camilo Rocha
# Se tuvo que preguntar como hacer la entrada a Juan sebastian Rivera y aconsejo como ignorar valores 
#https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc alli esta el comando for _ in range ...
## lo otro es lo mismo como mice and maze que se necesita inicio y una pos pero esta vez no compararla con un tiempo de salida 
## se vuelve y se hace uso de las librerias de montones de python heaps
def sssp(Grafo,inicio,pos):
  distancia = [ INF for _ in range(int(n)*int(m)) ]
  visited = [ False for _ in range(int(n)*int(m)) ]
  heap = [ (pos,inicio) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in Grafo[u]:
        if distancia[v]>d+w:
          distancia[v] = d+w
          heappush(heap,(distancia[v],v))
  return distancia

def main(delta): ## funcion lectura esta vez le entra el delta para hacer los if 
	global n,m,Grafo
	line = stdin.readline().strip()
	#print(line,"esto es line") check 
	#while len(line)!=0:
	for _ in range(int(line)):## ignora el index 
		n = stdin.readline().strip()
		m = stdin.readline().strip()
		#print(n,"esto es n") check
		#print(m,"esto es m") check 
		lista =[]
		Grafo = [[] for _ in range(int(n)*int(m))] ## crea el grafo o la matriz de nxm 
		for _ in range(int(n)): ## ignora index 
			lista.append([])
		for i in range(int(n)):
			fila =[ int(x) for x in stdin.readline().split() ]
			lista[i]=fila
		contador = 0
		for i in range(int(n)): ## dos for para moverme en la matriz
			for j in range(int(m)):
				Grafo[contador].append([contador,lista[i][j]])
				for dr,dl in delta: ## parte para verificar las fronteras 
					if i+dr >= 0 and i+dr<int(n) and j+dl>=0 and j+dl <int(m): ## que esten dentro de la matriz 
						if i+dr > i or i+dr < i:
							Grafo[contador].append([contador+(dr*int(m)),lista[i+dr][j]])
							#print(Grafo,"Asi va el grafo primera condicion")
						elif j+dl < j or j+dl > j:
							Grafo[contador].append([contador+dl,lista[i][j+dl]])
							#print(Grafo,"Asi va el grafo segunda condicion")
				contador = contador + 1
				#print("como va el contado",contador)
		ans = sssp(Grafo,0,lista[0][0])
		print(ans[int(n)*int(m)-1]) ## toca restarle 1 para que de se sale del rango 

main(delta)