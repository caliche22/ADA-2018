from sys import stdin

marble,lenm = None,None    (0,]

def solve(x):
  global marble,lenm
  pass

def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      x = int(inp.readline())
      ans = solve(x)
      print(ans)  # replace with the code below
      # if ans==-1 or marble[ans]!=x:
      #   print('{0} not found'.format(x))
      # else:
      #   print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()
