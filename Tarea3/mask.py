"""
Carlos Saul Arboleda 
0061863
Tarea3 Bit MAsk

Entrada: N entero de 32 bits, L y U, L <= U
Salida: Minimo valor de M, donde M es la mascara.

((N>>i)&1) == 0 Aqui detecto si el i-esimo bit está apagado, como está apagado se puede maximizar la mascara
Referencias https://wiki.python.org/moin/BitwiseOperators
"""

from sys import stdin

def solve(N,L,U):
	i,M = 31,0 ## i va hasta 32 bits 0-31
	while(i >= 0):
		MascaraSentinela = M|(1<<i) #Se prende el bit más signicativo, es decir, se enciende el i-ésimo bit de n
		if( (((N>>i)&1) == 0 and MascaraSentinela <= U) or MascaraSentinela<=L ):
			M=MascaraSentinela
		i-=1 
	return M #Mascara


def main(): ## entradas normales !! 
	inp = stdin
	line = inp.readline()
	global N,L,U ## variables enunciados
	while(len(line)!=0):
		N,L,U = [int(x) for x in line.split() ] 
		print(solve(N,L,U))
		line = inp.readline()
main()		
