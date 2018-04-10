# Carlos Saul Arboleda 
# 0061863
# Bank
# La idea es aplicar dijkstra en un arreglo de puntos
# de partida (nodos source) en donde la prioridad de 
# cada uno debe ser 0. 
# Código de sssp tomado de: https://drive.google.com/file/d/0B-Bk1ixpbgwJb0JiN1BiYWszWFU/view
# se hace uso del ssp del profesor y de las librerias por defecto de python de montones !!

from sys import stdin
from heapq import heappop,heappush

INF = float('inf') ## definicion de infinito

def sssp(G,source):
  """G is a graph representation in adjacency list format with vertices
     in the set { 0, ..., |V|-1 } and source a vertex in G"""
  # dist[u] : "minimum distance detected from source to u
  dist = [ INF for i in range(len(G)) ] ; 
  visited = [ False for i in range(len(G)) ]

  heap = []
  for i in range(len(source)):
    dist[source[i]] = 0 ## caso de distancia de el mismo de donde comienza
    heappush(heap,(0,source[i]))
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        dist[v] = min(dist[v],w+dist[u])
        if visited[v]==False:
          heappush(heap,(dist[v],v))
  return dist

def main():
    line = stdin.readline()
    global G 
    while len(line)!=0:
        N,M,B,P = [int(x) for x in line.split()] ## declaraciones de variables segun texto
        G = [list() for i in range(N)]
        for i in range(M):
            U,V,T = [int(x) for x in stdin.readline().split()]
            G[U].append((V,T));G[V].append((U,T)) 
        b,p = [0 for i in range(len(G))],[]
        tokb = stdin.readline().strip().split()
        for i in range(B): b[int(tokb[i])] = 1
        if P!=0:
          tokp = stdin.readline().strip().split()
          for i in range(P): p.append(int(tokp[i]))
        dist = sssp(G,p)
        S,E = 0,0 ## inicializo variables para compararlas con el arreglo que me devuelve dystra
        for i in range(N): 
            if b[i]==1: S = max(S,dist[i])## comparacion enunciado
        for i in range(N): 
            if S == dist[i] and b[i]==1: E += 1 ## comparacion2 enunciado
        if S == INF: print(E,'*') ## salida ejemplo enunciado
        else: print(E,S)
        for i in range(N):
            if S == dist[i] and b[i]==1: 
                E -= 1
                if E: print(i,'',end="")## salida enunciado vacio
                else: print(i)
        line = stdin.readline()
    
main()