from sys import stdin
## Carlos Saul Arboleda ADA Tarea2 Primes
## la idea es tener la lista de primos ya calculada por funcion o iniciarla a mano
## luego Hacer un cubo x,y,z para acceder mas rapido a los resultados que sirva por memorizacion con la funcion definida en clase
## se discutio el problema con Juan Miguel Cardona ,Juan Sebastian Rivera , Quiceno 

# primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
# 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 
# 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 
# 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 
# 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117]


cubote = 	[[[-1 for z in range(0,190)] for x in range(0,15)]for y in range(0,1121)] ## cubo segun las expecificaciones del problema 

def createPrimos(): ## funcion para inicializar los primos hasta un n
    global primos
    primos = []
    primos.append(2)
    i = 3
    while i < 1120:
        flag = False
        for k in range(2,i):
            if(i%k==0):
                flag  = True
                break
        if(flag == False):
            primos.append(i)
        i += 2
    return primos 

def solve(m,n,k): ## casos base y casos del profesor de la definicion del problema 
	if cubote[n][k][m] == -1:
		if n==0 and k == 0:
			cubote[n][k][m] = 1
		elif n!=0 and k==0:
			cubote[n][k][m] = 0
		elif m == 0:
			cubote[n][k][m] = 0		
		elif m!=0 and k!=0 and primos[m-1]>n:
			cubote[n][k][m] = solve(m-1,n,k)
		if m!=0 and k!=0  and primos[m-1]<=n:
			cubote[n][k][m] = solve(m-1,n,k)
			cubote[n][k][m] = cubote[n][k][m] + solve(m-1,n-primos[m-1],k-1)
	return cubote[n][k][m]

def main():
	global primos,n,k 
	n,k = -1,-1
	primos=createPrimos()
	line=stdin.readline()
	while len(line)!=0:
			line = line.strip()
			n,k = [ int(x) for x in line.split() ]
			if int(n) != 0 and int(k) !=0:
				print(solve(len(primos),n,k))
			line=stdin.readline() ## se me olvido leer aqui 

main()
#print(createPrimos(),len(primos)) #funciona se puede hacer con la raiz

