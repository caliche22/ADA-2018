## Carlos Saul Arboleda 
## 0061863
## Artic Kruscal
## se hace uso de la estructura dforest por metodo para aplicar kruscal visto en clase y poder resolver los satelites
## se necesita hallas las distancias por medio de hipotenusa y llevar la diferencia
## Se discutio el problema con Maria Paula y Juan Sebastian Rivera
from sys import stdin
import math



class dforest(object):

  def __init__(self,size=100):
    """create an emtpy forest"""
    self.__parent = [ i for i in range(size) ]
    self.__size = [ 1 for i in range(size) ]
    self.__rank = [ 0 for i in range(size) ]
    
  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return len(self.__parent)
  
  def __contains__(self,x):
    """return if x is an element of the forest"""
    return 0 <= x < len(self)

  def find(self,x):
    """return the representative of the tree of x"""
    assert x in self
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self,x,y):
    """make the union of the trees of x and y"""
    assert x in self and y in self
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      nx,ny = self.__rank[rx],self.__rank[ry]
      if nx<=ny:
        self.__parent[rx] = ry
        self.__size[ry] += self.__size[rx]
        if nx==ny: self.__rank[ry]+=1
      else:
        self.__parent[ry] = rx
        self.__size[rx] += self.__size[ry]
        
  def size(self,x):
    """return the size of the tree of x"""
    assert x in self
    return self.__size[self.find(x)]

def kruskal(Grafo,diferencia):
  """G is a connected graph in adjacency list representation. For each
  vertex u in G, G[u] is the list of pairs (v0,w0),...(vn,wn) such that
  there is an edge between u and vi with weight wi (0 <= i <= n)"""
  edges = list()
  #print(diferencia,"la diferencia" )
  for i in range(len(Grafo)):               # collect the edges in G
    for v,w in Grafo[i]:
      if (w!=-1):
        edges.append((i,v,w))
  # sort the edges in ascending order w.r.t weights in the edges
  edges.sort(key=lambda x: x[2])## se organiza por peso       
  ans,sans = [ list() for i in range(len(Grafo)) ],0
  df = dforest(len(Grafo))
  i = 0
  contador=0
  while i!=len(edges):
    u,v,w = edges[i]
    if df.find(u)!=df.find(v):
      df.union(u,v)
      contador+=1
      if(contador==diferencia):
        #print (w,"pinche w")
        return w

    i += 1

def main():
  global Grafo,satelites,torres,diferencia
  line=stdin
  casos = int(stdin.readline().strip())
  #print(casos,"la linea")
  while casos!=0:
    line = stdin.readline().strip().split()
    satelites,torres= int(line[0]), int(line[1])
    #print("satelites, torres",satelites,torres)
    diferencia=torres-satelites
    lista=list()
    while(torres!=0):
      line=stdin.readline().strip().split()
      cordx,cordy= int(line[0]),int(line[1])
      #print("cordenas ",cordx,cordy)
      lista.append((cordx,cordy))
      #print("la pinche lista ",lista)
      torres-=1
    index=0
      #print("cuanto van las torres",torres)
    listaadyacencia=[ [(index,-1) for index in range(len(lista))]  for index in range(len(lista))]
    while(index!=len(lista)):
      j=index+1
      while(j!=len(lista)):
        distancia=math.hypot(lista[index][0]-lista[j][0],lista[index][1]-lista[j][1])
        listaadyacencia[index][j]=(j,distancia)
        j+=1
      index+=1
    casos-=1
    print('{:.2f}'.format(kruskal(listaadyacencia,diferencia)))

main()
