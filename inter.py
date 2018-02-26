from sys import stdin
## Carlos Saul Arboleda ADA Tarea2 #interview 
## se hace uso del codigo trip del enunciado y se pasa a una funcion solve y se utiliza una matriz de 61*61 
## para que nos ayude de manera de memorizacion y se retorna memo 
## se castea para poder imprimir bien 
## Se discutio el problema con Juan Sebastian Rivera y los comentarios del profesor en clase 'back'



memo=[[0 for x in range(0,61)]for y in range(0,61)] ### dinamica por memorizacion se utiliza una matriz y como se maneja numeros se llena de 0 
def solve(n,k):## transcripcion del codigo de interview funcion trip con sus condicionales 
	global memo
	if n<=1: ## condicion enunciado
		return 1
	else:
		if memo[n][k]!=0:
			return memo [n][k]
		else:
			memo[n][k]= 1
			for i in range(1,k+1):
				memo[n][k]= memo[n][k]+solve(n-i,k) ## funcion trip mostrada en el enunciado
			return memo[n][k]



def main():
	global memo,n,k
	line=stdin.readline() ## variable para leer 
	n,k,contador = 0,0,1
	while(len(line)!=0): ### condicion para leer
			##line = stdin.readline().strip() ## para que lea y parta en 
			n,k = [ int(x) for x in line.split() ] ## variables del enunciado 
			if(n<61): ## condicion para calcular del enunciado
				#print("Case {}: {}".format(contador,solve(n,k))) ## imprimir todo de una No me dio
				contador=str(contador)
				print("Case",contador+":",solve(n,k))## falto los benditos espacios
				contador = int(contador) + 1
				#line=stdin.readline() ## leo siguiente linea estaba leyendo mal estaba leyendo doble
			line=stdin.readline() ## leo asi no entre para que pare de leer

main()