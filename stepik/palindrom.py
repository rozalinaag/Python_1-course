#Two interesting ways to solve finding a palindrome

print("Input line:")
stroka = input()
if(stroka==stroka[::-1]):
  print("YES")
else:
  print("NO")
  
#Another way, more productive
print("Another way:")

i=0
j=len(stroka)-1
flag = True
while(i<j):
  if (stroka[i]!=stroka[j]):
    flag=False
  i+=1
  j-=1
if (flag):
  print('YES')
else:
  print('NO')
