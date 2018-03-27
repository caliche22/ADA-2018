from sys import stdin
import math
## Carlos Saul Arboleda Tarea1 ADa
## Codigo 0061863
## Se hace uso de funciones de UltraQuickSort de la Tarea1 merge y mergesort el merge se tiene que modificar con lo recomendado con el profesor
## Se le pidio ayuda a Juan Miguel Cardona
EPS,points = 1e-9,None

def merge(): ### forma del profesor que explico arreglar primero arreglo x luego armar la tripla y luego acomodar el y
  aux=[]
  global points
  points.sort
  mergesort(0,len(points))
  for i in range(low,mid):
      pass ## va la magia del profesor explicada en clase
  return 0.0


def distancia(x,y,x1,y1): ## formula de distancia ,se puede hacer hipotenusa o aplicando formula
    return math.sqrt((x-x1)**2+(y-y1)**2)

def mergesort(low,hi): ## se utiliza el mergesort del ultra quick sort por que es la misma forma de organizar pueden haber casos cruzados
    if low+1 != hi:
        mid= low+((hi-low)>>1)
        mergesort(low,mid)
        mergesort(mid,hi)
        solve(low,mid,hi)

def AloBruto(left,right,points): ## estilo 2 de algoritmo a fuerza bruta presentado por el profesor como opcion al solve
    valores=None
    epspos=1e99
    for i in range(0,right-1):
        for j in range(i+1,right):
            dis=distancia(points[i][0],points[i][1],points[j][0],points[j][1])
            if dis<(epspos):
                epspos=dis
    return epspos



def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1])))
    ans = merge()
    if(ans<10000): ## caso del enunciado del pdf
        print('{:.4f}'.format(ans))
    else:
        print("INFINITY") ## caso del enunciado del pdf
    n = int(stdin.readline())

main()
