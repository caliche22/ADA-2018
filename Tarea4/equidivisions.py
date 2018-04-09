"""
Carlos Saul Arboleda
0061863
--Función Solve--
Entrada: Matriz cuadrada, con eĺ tamaño de filas y columnas
Salida: Dice si una matriz cuadrada es una equidivision

Se hace uso del algoritmo floodfill o algoritmo de relleno por difusión el cual consiste en determinar
el area formada por elementos contiguos en una matriz multidimensional.

Referencias:
- https://drive.google.com/file/d/0B-Bk1ixpbgwJV2VQNkhEaFh3Qk0/view
"""
from sys import stdin

#[drow,dcol] en estos arrelgos no se tiene en cuenta las diagonales 1,1 0,0
drow = [ -1, 0, 1, 0 ]
dcol = [ 0, 1, 0, -1 ]

def fill(row,col,visited,rows,cols):
  assert visited[row][col]==0
  global tableroarray
  stack = [ (row,col) ] ; visited[row][col] = 1
  rContinua = 0 #rContinua = región continua
  while len(stack)!=0:
    r,c = stack.pop()
    rContinua += 1
    for i in range(len(drow)):
      rtmp,ctmp = r+drow[i],c+dcol[i]
      if 0<=rtmp<rows and 0<=ctmp<cols and tableroarray[rtmp][ctmp]==tableroarray[r][c] and visited[rtmp][ctmp]==0:
        stack.append((rtmp,ctmp)) ; visited[rtmp][ctmp] = 1
    visited[r][c] = 2
  return rContinua

def solve(rows,cols):
	global tableroarray
	ans = True
	visited =  [ [ 0 for c in range(cols) ] for r in range(rows) ]
	for r in range(rows):
		for c in range(cols):
			if visited[r][c] == 0 and fill(r,c,visited,rows,cols)!= rows:
				ans = False	
	if ans == False:
		print("wrong")
	else:
		print("good")

def main():
	inp = stdin
	line = int(inp.readline())
	global tableroarray
	while line != 0:
		tableroarray = [ [ 0 for c in range(line) ] for r in range(line) ]
		for r in range(line-1):
			partition = [ int(x) for x in inp.readline().split() ]
			posx,posy = 0, 1
			bandera = True
			for c in range(line):
				if bandera == True:
					x, y = partition[posx],partition[posy]
					bandera = False
				else:
					posx += 2 ;	posy += 2
					x, y = partition[posx], partition[posy]
				tableroarray[x-1][y-1] = r+1
		#print("AQUI va line",line)		
		solve(line,line)
		#print("AQUI va el arreglo",tableroarray)
		line = int(inp.readline())
main()	