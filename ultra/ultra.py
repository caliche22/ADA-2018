###Carlos Saul Arboleda ADA Tarea1

##MergeSort implementacion codigo
#assert i==hi and l==mid and r==hi 
## se implementa el codigo del profesor con las variantes de los contadores para poder hacer bien 
## los cambios de menor a mayor
# el problema se discutio con Sebastian Quiceno - Juan Sebastian Rivera - cuaderno Maria Paula 
from sys import stdin
MAX=50010
num=[None for i in range(MAX)]
aux=[None for i in range(MAX)]

def solve(low,hi):
	global num
	cuenta=0
	if low+1 < hi:
		mid=low+((hi-low)>>1)
		cuenta=cuenta+solve(low,mid)## lado izquierdo cuenta
		cuenta=cuenta+solve(mid,hi)## lado derecho cuenta
		cuenta=cuenta+merge(low,mid,hi) ## caso del medio cruzado cuenta
	return cuenta

def merge(low, mid, hi):
	global aux, num
	contador=0
	for i in range(low,hi):
		aux[i]=num[i]
	l,r,i=low,mid,low
	while i!= hi:
		if l!=mid and r!=hi:
			if aux[l]<=aux[r]:
				num[i]=aux[l]
				l+=1
			else:
				num[i]=aux[r]
				r+=1
				contador=contador+(r-(i+1))
		elif r==hi:
			num[i]=aux[l]
			l+=1
		else:
			num[i]=aux[r]
			r+=1
		i+=1
	return contador
#assert i==hi and l==mid and r==hi 


def main(): ## template profesor !! de lectura
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      num[i] = int(stdin.readline())
      #solve(0,n)
    print(solve(0, n))
    n = int(stdin.readline().strip())

main()