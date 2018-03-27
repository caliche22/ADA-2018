from sys import stdin

#Carlos Saul Arboleda
#0061863
#Se Discutio con Juan Fernando Escobar, Juan Sebastian Rivera cambiar todos los ? a ceros 
## teniendo en cuenta cuando sos h secuencia 100 , 10 forma de arbol vista en clase 

def solve(lista):
	contador = 0
	total = 0
	cuenta = 0
	while contador <len(lista): ## no es igual se sale del rango 
		if lista[contador]=='?':
			lista[contador] = '0'
		if lista[contador]=='1':
			if cuenta == 0:
				cuenta = cuenta + 3 ## 100
				#print("entro cuenta 0",cuenta) check 
			else:
				cuenta = cuenta + 1 ## 10
				#print("entro else cuenta 0",cuenta) check 
		if lista[contador]=='0':
			if cuenta == 0:
				total = total + 1
			else:
				cuenta = cuenta -1
				#print("entro else2 cuenta 0.2",cuenta) check 
		if cuenta == 1:
			cuenta=0
			total = total + 1
		contador = contador+1
	if cuenta == 0:
		return total
	return 0




def main():
	line = '1'
	global lista
	while line!= '':
		line = stdin.readline().strip()
		if line!='':
			#lista=[]
			lista =list(line)
			#lista.append(line) ## esta cosa no servia
			#print("la lista de caracteres",lista)
			print(solve(lista))
			

main()