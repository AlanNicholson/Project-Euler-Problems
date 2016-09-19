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
