#Carlos Saul Arboleda ADA Tarea1
#codigo	0061863
from sys import stdin

MAX = 610
sites = [ None for i in range(MAX) ]
sums,minn,maxx,n,k = None,None,None,None,None ## inicializacion estilo profesor

def solve(sites):
  #distancia entre cada sitio
  #sums suma de todo los sitios es el maximo
  #minn # distancia minima
  #maxx #distancia maxima
  #n es el numero de sitios
  #k es el numero de noches
  
  
  #el algoritmo se basa en en recortar los valores de busqueda
  #empezando con el la suma de todas las ditancias como el maximo  y evaluando (hi + low) //2
  #apartir de ahi cada numero se prueba con la distancia minima y se empieza a restar el numero de noches "k"
  #si pasa la prueba responde true y hi es igual a esa posicion si la prueba termina en false low=mid
  #el algoritmo termina cuendo (low+1 != hi)
  sites1=sites[:n]
  hi = sums
  low = 0
  while(low+1 != hi):
    mid = (hi + low) //2
    if(comparacion(mid,k,sites1)):
      hi = mid
    else:
      low = mid
  return hi

def comparacion(mid,k,sites1):
    #se toma un valor igual a que se encontro con la funcion y si puede pasar se le resta la posicion de la lista que paso
    #si al final termina puede recorrer todo en "k" noches retorna true de lo contrario retorna false
    val = mid
    i=0
    while i<len(sites1):
      if(val >= sites1[i]):
        val = val - sites1[i]
      elif(k > 0 and mid >= sites1[i]):
        val = mid - sites1[i]
        k= k-1
      else:
        return False
      i=i+1
    return True



def main(): ## template profesor 
  global sites,sums,minn,maxx,n,k
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    minn,maxx,sums = float('inf'),float('-inf'),0
    for i in range(n):
      sites[i] = int(inp.readline().strip())
      if sites[i]>maxx: maxx = sites[i]
      if sites[i]<minn: minn = sites[i]
      sums += sites[i]
    if sums==0:
      print(0)
    else:
      print(solve(sites))
    l = stdin.readline().strip()

main()