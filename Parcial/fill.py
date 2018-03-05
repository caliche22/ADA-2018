#Parcial 1
#ADA Carlos Saul Arboleda
#Fill

## Tres funciones main solve( binary search ) y una para comparar si si se puede o no 
from sys import stdin


def comparar(mid): ## booleana si se puede llenar los containers o no
	global listavesels,m
	container=1
	capacidad=mid
	i=0
	#print(mid,"el mid antes ")
	#print(capacidad,"capacidad antes")
	while i<len(listavesels):
		#print("HOLA soy una bandera voy por aqui bien")
		if(listavesels[i]>mid):  ## ningun container puede tener tanta leche
			#print("listavesels",listavesels[i])
			#print("entro primer if")
			return False
		if(listavesels[i]>capacidad):
			#print("entro segundo if")
			if (container==m): ## todos los containers estan llenos
				#print("entro en el if anidado")
				return False
			container=container+1
			#print(container," el container")
			capacidad=mid
			#print(capacidad,"la capacidad")
		capacidad=capacidad-listavesels[i]
		i=i+1
	return True
	#pass

# def comparar2(mid):
# 	global listavesels,m
# 	container1=1
# 	for i in range(len(listavesels)):
# 		if listavesels[i]>mid:
# 			return False
# 		if container1+listavesels[i]>mid:
# 			container1=0
# 		if container1==0:
# 			container1=container1+1
# 		if container1>m:
# 			return False
# 		container1+=listavesels[i]
# 	return True
	#pass

def binarySearch():
	global listavesels,m
	ans,low,hi=0,1,1000000000
	#ans=hi+1
	#low=listavesels[0] ## esto no sirve
	#hi=n
	while low<=hi: ## lo tenia antes low!=hi, low <= hi
		mid=low+((hi-low)//2)
		##print(mid,"LLEGA AQUI se caga en el if ")
		if comparar(mid)==True:
			#print("entra??")
			ans=mid
			#print("esto vale ans",ans)
			#print("esto vale mid",mid)
			#print("esto vale low",low)
			hi=mid-1
			#print("esto vale hi",hi)
		else:
			#print("entra a false")
			low=mid+1
			#print("Esto vale low",low	)
	return ans
	#pass

def main(): ### lectura check bonito
	global n,m,listavesels
	line=stdin.readline() 
	while len(line)!=0:
			#line = line.strip()
			n,m = [ int(x) for x in line.split() ]## los vesels y los cotainer
			line=stdin.readline()
			listavesels = [ int(y) for y in line.split() ]
			#print (n,m)## check
			#print(listavesels)## check 
			print(binarySearch())
			line=stdin.readline() ## se me olvido leer aqui

main() 