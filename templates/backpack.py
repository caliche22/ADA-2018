from sys import stdin

MAX = 610
sites = [ None for i in range(MAX) ]
sums,n,k = None,None,None

def solve():
  global sites,n,k
  pass

def main():
  global sites,n,k
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    for i in range(n):
      sites[i] = int(inp.readline())
    print(solve())
    l = stdin.readline().strip()

main()
