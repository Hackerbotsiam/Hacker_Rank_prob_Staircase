# Staircase
def Staircase(n):
  for i in range(1 , n+1):
    gap= " "* (n-i) # creat gap
    hash= "#"*i     # creat hash
    result= gap + hash # combination of hash and gap
    print(result)




n= int(input()) # Enter here the total staircase
Staircase(n)