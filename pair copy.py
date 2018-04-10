from sys import stdin
import math

EPS,points = 1e-9,None

def distance(x1 , y1 ,x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def merge_sort(low, hi):
 if low+1 != hi:
    mid = low+((hi-low)//2)
    merge_sort(low, mid)
    merge_sort(mid, hi)
    merge(low, mid, hi)

def merge(p, q, r):
  # copy the subarray A[p,q) into a1
  global points
  a1 = list()
  for i in range(p, q):
    a1.append(points[i])
  # copy the subarray A[q,r) into a2
  a2 = list()
  for i in range(q, r):
    a2.append(points[i])
  n1,n2 = q-p,r-q
  assert n1==len(a1) and n2==len(a2)
  i1,i2,n = 0,0,r-p
  assert n==n1+n2
  for j in range(p, r):
    # sort the subarray A[p,r)
    if i1<n1 and i2<n2:
      # if both temporary arrays have not been processed entirely
      if a1[i1][1] < a2[i2][1]:
        points[j] = a1[i1]
        i1 += 1
      else:
        points[j] = a2[i2]
        i2 += 1
    elif i1<n1:
      # temporary array a2 has been processed entirely but not a1
      points[j] = a1[i1]
      i1 += 1
    else:
      # temporary array a1 has been processed entirely but not a2
      points[j] = a2[i2]
      i2 += 1
  assert i1==n1 and i2==n2


def fuerzaBruta(l,r):
    men = 1e99
    valores = None
    for i in range(0,r-1):
        for j in range(i+1,r):
            a = distance(points[i][0],points[i][1],points[j][0],points[j][1])
            if( a < men):
                men = a
    return men




def divide(l,r):
    if((r-l) == 2):
        return distance(points[l][0],points[l][1],points[r-1][0],points[r-1][1])


    elif(r-l == 1):
        return   1e99
    else:
        mid = l+(r-l)//2
        L = divide(l,mid)
        R = divide(mid,r)

        p = max(points[l:mid])
        q = min(points[mid:r])

        k = min(points[l:mid])
        z = max(points[mid:r])

        ut = min(points[l:mid])
        ot = min(points[mid:r])

        bt= max(points[l:mid])
        xt= max(points[mid:r])

        jn = fuerzaBruta(p[0],q[1])

        cs = distance(k[0],k[1],z[0],z[1])
        ts= distance(p[0],p[1],q[0],q[1])
        qs= distance(ut[0],ut[1],ot[0],ot[1])
        at= distance(bt[0],bt[1],xt[0],xt[1])
        d = min(L,R,cs,ts,qs,at)

    return d


def solve():
  global points
  global men
  global y
  y = list()
  points.sort()
  dx = divide(0,len(points))
  merge_sort(0,len(points))
  dy = divide(0,len(points))
  return min(dx,dy)

def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1])))
    ans = solve()
    if(ans < 10000):
         print('{:.4f}'.format(ans))
         #pass
    else:
          print("INFINITY")
          #pass
    n = int(stdin.readline())

main()

##https://www.cs.mcgill.ca/~cs251/ClosestPair/ClosestPairDQ.html#
