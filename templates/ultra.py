from sys import stdin

MAX   = 50010
num   = [ None for i in range(MAX) ]

def solve(low, hi):
  pass



def main():
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      num[i] = int(stdin.readline())
      print(num)
    #print(solve(0, n))
    n = int(stdin.readline().strip())

main()
