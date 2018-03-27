from sys import stdin

EPS,points = 1e-9,None

def solve():
  global points
  return 0.0

def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1])))
    ans = solve()
    print('{:.4f}'.format(ans))
    n = int(stdin.readline())

main()
