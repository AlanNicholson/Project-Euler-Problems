#https://projecteuler.net/archives
#Problem 1: Multiples of 3 and 5
total=[]
for i in range(0,1000):
      if i % 3 ==0 or i % 5 ==0:
            total.append(i)
print(sum(total))
#Problem 2: Even Fibonacci numbers
fibL=[0,1]
fibLeV=[]
x=int(input("Fibonacci up to: "))
for i in range(2,30000):
      fibL.append(fibL[i-1]+fibL[i-2])
      if len(fibL)>=500:
            break
for a in fibL:
      if a % 2 ==0:
            if a <= 4000000:
                  fibLeV.append(a)
print(fibL, sum(fibLeV))
# Problem 3: Largest Prime Factor
def lPf(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
b=int(input("Largest Prime Factor of: "))
print(lPf(b))
# Problem 4: Largest Palindromic Number
paList=[]
for a in range(10,1000):
    for b in range(10,1000):
        if str(a*b)==str(a*b)[::-1]:
            paList.append(int(a*b))
print(max(paList))
# Problem 5: Smallest Multiple of 1 to 20
print("Answer is: ",(16*9*5*7*11*13*17*19)) # Think of py way of explaining 16 and 9
# Problem 6: Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.
bL=[]
d=(sum(range(1,101)))**2
for i in range(1,101):
    if i < 101:
        bL.append(i**2)
print(d-(sum(bL)))
# Problem 7: 10001st Prime
allP=[x for x in range(2,105000)
      if all(x % y != 0 for y in range(2,x) )]
print("The 10001st Prime is: ",allP[10000]) # Not ideal. Took 2min 40sec
