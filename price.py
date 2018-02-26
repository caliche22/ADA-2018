from sys import stdin
## Carlos Saul Arboleda ADA Tarea2 Price 
## Se hace uso de los apuntes de Maria Paula y de la Explicacion del profesor con su 
## tabulacion 
## Maria paula y Quiceno me aconsejaron comenzar a leer si no es vacio lea 

tab=[[0 for x in range(0,301)]for y in range(0,301)] ## dimensiones de la matriz dadas por el enunciado y criterio de 300 visto en clase
tab[0][0]=1 ## posicion dada cuando se tabula cuanto tiene que ser


def tabulacion(tab): ## tabulacion apuntes Maria Paula hecha por el profesor en clase
	m,n,l = 1,0,1
	while(m !=301):
		if(l == 301):
			m,n,l=m+1,0,1
		elif(n== 301):
			n,l=0,l+1
		else:
			if(m<=n):
				tab[l][n] = tab[l][n]+tab[l-1][n-m]
			n = n + 1
	return tab


def main():
	tabu=tabulacion(tab)
	line = '-1' ## inicializarlo en algo
	while(line!=''): ## mientras no sea vacio
		line = stdin.readline().strip()
		lista = [ int(x) for x in line.split() ]
		#print("essta mierda es la lista ",lista )
		ans=0
		if(len(lista) >=1):
			if(len(lista)==1): #Caso 1 
				for i in range(0,int(lista[0]+1)):
					ans = ans + tabu[i][lista[0]]
					#print(ans,"el caso 1") 
			elif(len(lista)==2): #Caso 2
				for i in range(0,min(int(lista[1])+1,int(lista[0]+1))):
					ans = ans + tabu[i][lista[0]]
					#print(ans,"el caso 2")
			elif(len(lista)==3): #Caso 3
				for i in range(int(lista[1]),min(int(lista[2])+1,int(lista[0])+1)): ## caso que se casca !!
					ans = ans + tabu[i][lista[0]]
					#print(ans,"el caso 3") 
			print(ans)
		#line.stdin.readline() no sirvio


main()