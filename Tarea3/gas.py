# Carlos Saul Arboleda
# 0061863 Tarea3 Gas

## Problema resuelto en clase con la ayuda del profesor que dijo que se hacia en 5 minutos , se discutio el problema con Juan sebastian rivera
## y Juan Fernando Escobar 
## Se hace uso del codigo del profesor mic_wf de su repositorio
## Se hace uso de la resta y suma para ver que tanto cubren del trayecto y o segmento --x-y----x+y----- asi sucesivamente
## 
from sys import stdin


def mic_wf(L,H,a): ## codigo del profesor Camilo Rocha visto en clase 
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return len(ans) #Se retorna la cantidad de estaciones que se utilizan, si es 0 es porque algun segmento del trayecto no se puede cubrir 




def main():
	line=stdin.readline() 
	while len(line)!=0:
		l,g = [ int(x) for x in line.split() ]
		#print(l,g,"l y g")
		if l!=0 and g!=0: ## nos aseguramos que los dos sean distintos a 0 para poder hacer las restas y sumas conrespondientes
			lista =[] ## lista para mandar a la funcion del profesor
			for i in range(g):
				line = stdin.readline().strip()
				x,y = [ int(x) for x in line.split() ]
				#print(x,y,"los x , y , las duplas ")
				lista.append([x-y,x+y])
				#print(lista,"se mete en la lista")
			ans= mic_wf(0,l,lista)### funcion profesor
			if ans == 0:   #si es 0 es porque un segmento no se cubrio y se retorna -1 haciendo enfasis que no se puede
				print(-1)
			else: #De lo contrario, la cantidad de estaciones a eliminar, es la cantidad total de estaciones menos las que necesito dicho por el profesor en clase y ya :D.
				print(g-ans)
		line=stdin.readline() 


main()

