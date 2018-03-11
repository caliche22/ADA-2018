# Carlos Saul Arboleda
# 0061863 install

# Entrada: Una lista de duplas, donde las duplas vienen con las coordenas X,Y.
# Salida: Mínimo número de instalaciones de radar para cubrir todas las islas dadas.

# Referencias:
# - https://bitbucket.org/snippets/hquilo/x6p5x/activity-scheduling-algorithm-greedy
#   Se hace uso de la misma lógica del problema greedy de agendamiento de actividades,
#   donde  las coordenadas que se envian son (x - d,x + d), haciendo uso del teorma de
#   pitagoras de apoyo.Si tenemos el caso donde d < posición en Y,
#   no es posible cubirir la isla con el radar por ende se retorna -1


import math
from sys import stdin

def solve(coordenadas):
	coordenadas.sort(key=lambda x : x[1]) ## ordenadas por el segundo componente Y
	ans,n,N = 0,0,len(coordenadas)
	while n!=N:
	  best,n,ans = n,n+1,ans+1
	  while n!=N and coordenadas[n][0]<coordenadas[best][1]:
	    n += 1
	return ans
	
def main():
	inp = stdin
	line = inp.readline()	
	numeroIslas, distanciaCubierta = [ int(x) for x in line.split() ]
	cases = 1
	while(numeroIslas != 0 and distanciaCubierta != 0):
		coordenadas = []
		radioMY = False #radio menor que la coordenada Y
		for i in range(numeroIslas):
			lineaX, lineaY = [ int(x) for x in inp.readline().split() ]
			cateto  = (distanciaCubierta**2)-(lineaY**2) #Se obtiene un cateto 
										
			if(distanciaCubierta < lineaY or cateto < 0): #Caso1
				radioMY = True
			elif(lineaY == distanciaCubierta): #Caso2
				coordenadasXY = [lineaX-distanciaCubierta,lineaX+distanciaCubierta]
				coordenadas.append(coordenadasXY)
			else:					
				coordenadasXY =	[lineaX - math.sqrt(cateto),lineaX + math.sqrt(cateto)]
				coordenadas.append(coordenadasXY)
				
		if(radioMY == True): ## Caso no posible
			print("Case"+" "+str(cases)+":"+" "+"-1")
			cases+=1
		else:
			print("Case"+" "+str(cases)+":"+" "+str(solve(coordenadas))) ## de lo contrario calcular
			cases+=1
		line = inp.readline()
		numeroIslas, distanciaCubierta = [ int(x) for x in inp.readline().split() ]

main()