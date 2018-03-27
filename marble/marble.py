#Carlos Saul Arboleda ADA Tarea1
#Codigo 0061863


from sys import stdin

marble,lenm = None,None #inicializacion estilo profesor 

def solve(x,marble,lenm):
  low = 0
  hi = len(marble)-1
  ans1 = False
  while low <= hi :
    mid = int(((hi+low))/2) ## casteo a entero
    if marble[mid] == x: ## esta exactamente en la mitad
      pos = mid ## guardar la pos para luego imprimir 
      ans1 = True
      hi = mid-1
    elif marble[mid] > x:
        hi = mid-1
    else:
        low = mid+1
  if ans1== True:
    return pos
  else:
    return -1 ## caso de que no este en todo el arreglo 

def main():
  global marble,lenm ## para pasarselo a la funcion solve
  inp = stdin
  case = 1 ## para imprimir los casos 
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort() ## organizar la lista para que sirva el binary search
    print('CASE# {0}:'.format(case))
    for q in range(lenq):
      x = int(inp.readline())
      ans = solve(x,marble,lenm)
      if ans==-1 or marble[ans]!=x: ## condicion de que no este encontrado y no se halla encontrado el elemento  decir not found
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    case += 1

main()

