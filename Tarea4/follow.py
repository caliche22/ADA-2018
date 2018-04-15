from sys import stdin
# Carlos Saul Arboleda
#0061863
#Trabajado con Juan Fernando Escobar, Maria Paula Carrero, Juan Sebastian Rivera
#El algoritomo es dar todos los ordenes topologicos se tiene que modificar el algoritmo topo
# y ir sacando todos los posibles ordenes por medio de variables temporales
## se hace uso de .ord que lo que hace es ord() es dar el codigo ASCII de cada caracter y char para poder
## cambiar de ascii a caracter 
## las referencias de ascii se saca https://www.quora.com/What-is-the-use-ord-and-chr-in-python 

## idea principal 
# def toposort(G, indeg):
#   ans,cand = list(),list()
#   for u in range(len(indeg)):
#     if indeg[u]==0: cand.append(u)
#   while len(cand)!=0:
#     ans.append(cand.pop())
#     for v in G[ans[-1]]:
#       indeg[v] -= 1
#       if indeg[v]==0: cand.append(v)
#   return (len(ans)==len(indeg), ans)


  
def topos(indeg,ans,contador): ## funcion para sacar todos los ordenes topologicos
	global lista1,lista2,resultado
	candidatos =[]
	for u in range(len(indeg)):
		if indeg[u]==0:
			valor = chr(u+97) ## cambia ascii a letra caracter
			candidatos.append(valor)
	anstemporal = ans
	contador = contador+1
	for i in range(len(candidatos)):
		opcion = candidatos.pop()
		anstemporal = ans + opcion
		if contador == len(lista1):
			resultado.append(anstemporal)
		else:
			indegtemporal = indeg[:]
			letra = ord(opcion)-97 ## ascii
			indegtemporal[letra] = indegtemporal[letra]-1
			for i in range(len(lista2)):
				if opcion == lista2[i][0]:
					letra = ord(lista2[i][1])-97 ## ascii
					indegtemporal[letra] = indegtemporal[letra]-1
			topos(indegtemporal,anstemporal,contador)


def main():
	global lista1,lista2,resultado,palabra
	lista1,lista2,resultado = None,None,None
	line = "-1"
	while line != "":
		total = 0
		line = stdin.readline().strip()
		if line != "":
			indeg =[]
			lista2 =[]
			contador = 0
			lista1= [x for x in line.split() ]
			palabra= [-1 for x in range(26) ]
			line = stdin.readline().strip().split()
			lista1.sort()
			for i in lista1:
				letra = ord(i)-97 ## letra a ascii
				palabra[letra]=0
			while contador < len(line):
				lista2.append([line[contador],line[contador+1]])
				letra = line[contador+1]
				palabra[ord(letra)-97]=palabra[ord(letra)-97]+1
				contador+= 2
			resultado =[]
			topos(palabra,'',0)
			total = len(resultado)
			if total != 0:
				for i in range(1,total+1):
					print(resultado[total-i])
				print("")

main()