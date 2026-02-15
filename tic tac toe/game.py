import math
b=[" "]*9
H,A="X","O"
def p():print("\n".join([" | ".join(b[i*3:(i+1)*3]) for i in range(3)]))
def w(ply):return any(all(b[i]==ply for i in c) for c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
def d():return" " not in b
def minimax(mx,alpha,beta):
 if w(A):return 1
 if w(H):return-1
 if d():return 0
 if mx:
  s=-math.inf
  for i in range(9):
   if b[i]==" ":
    b[i]=A
    s=max(s,minimax(False,alpha,beta))
    b[i]=" "
    alpha=max(alpha,s)
    if beta<=alpha:break
  return s
 s=math.inf
 for i in range(9):
  if b[i]==" ":
   b[i]=H
   s=min(s,minimax(True,alpha,beta))
   b[i]=" "
   beta=min(beta,s)
   if beta<=alpha:break
 return s
def ai():
 s=-math.inf;mv=0
 for i in range(9):
  if b[i]==" ":
   b[i]=A
   v=minimax(False,-math.inf,math.inf)
   b[i]=" "
   if v>s:s,mv=v,i
 b[mv]=A
def hu():
 while 1:
  try:
   x=int(input("1-9:"))-1
   if 0<=x<=8 and b[x]==" ":b[x]=H;break
  except:pass
def g():
 print("You:X AI:O")
 while 1:
  p();hu()
  if w(H):p();print("You win");break
  if d():print("Draw");break
  ai()
  if w(A):p();print("AI wins");break
  if d():print("Draw");break
g()
