##print("Hello World")
##print("This is DELL")



##a=int(input())
##b=int(input())
##a=str(a)
##a=list(a)
##c=[]
##e=0
##for i in range(b):
##    c.append(max(a))
##    a.remove(max(a))
##d=[int(i) for i in c]
##for j in range(len(d)):
##    e=e*10+d[j]
##print(e)



##a=list(map(int,input().split()))
##b=len(a)
##c=set(a)
##c=list(c)
##for i in range(len(c)):
##    d=a.count(c[i])
##    if d>(len(a)//2):
##        print(a[i])
##        break
    
##a="LOVELY"
##if a.upper():
##    a=a.lower()
##print(a)



##s=input()
##t=input()
##s=list(s)
##t=list(t)
##a=len(t)
##c=0
##for i in range(len(s)):
##    if s[i] in t:
##        c+=1
##        t.remove(s[i])
##if c==a and c==len(s):
##    print("Given string is ANAGRAM")
##else:
##    print("Given string is NOT ANAGRAM")
        

            
##n=5
##ar=[81,25,27,32,51]
##B=[]
##C=[]
##for i in range(len(ar)):
##    for j in range(2,ar[i]):
##        if ar[i]%j==0:
##            a=ar[i]//j
##            print(j)
##            B.append(j)
##            break
##        
##    d=0
##    while ar[i]!=1:
##        c=ar[i]//j
##        d+=1
##        ar[i]=c
##    C.append(d)
##    print("D",d)
##    
##print("B",B)
##print("C",C)
##A=[]
##for i in range(len(ar)):
##    for j in range(len(B)):
##        for k in range(len(C)):
##            if i==j==k:
##                ab=pow(B[j],C[k])
##                print(ab)
##                if ab==ar[i]:
##                    A.append(ab)
##print(A)



##def individuals(A):
##    C=0
##    while A!=0:
##        r=A%10
##        C+=r
##        A=A//10
##    return C
##        
##
##
##r=c=int(input())
##matrix=[[int(input()) for i in range(c)] for j in range(r)]
##ele=int(input())
##Sum=0
##for i in range(r):
##    for j in range(c):
##        if ele==matrix[i][j]:
##            Sum=i+j
##if Sum%2==0:
##    b=0
##    for i in range(r):
##        for j in range(c):
##            if matrix[i][j]%2==0:
##                b+=individuals(matrix[i][j])
##    print(b)
##else:
##    b=0
##    for i in range(r):
##        for j in range(c):
##            if matrix[i][j]%2==1:
##                b+=individuals(matrix[i][j])
##    print(b)




##n,x=map(int,input().split())
##n=str(n)
##a=n[:x]
##b=n[-x:]
##a=int(str(a))
##b=int(str(b))
##print(abs(a-b))



##n=int(input())
##c=n
##a=0
##while n!=0:
##    r=n%10
##    b=1
##    for i in range(1,r+1):
##        b*=i
##    a+=b
##    n=n//10
##if c==a:
##    print("Strong Number")
##else:
##    print("Not Strong Number")




##n=str(input())
##a=[]
##for i in range(len(n)):
##    a.append(n[i])
##a=sorted(a)
##print(a[0])




##def FindSum(n,k):
##    Sum=0
##    a=1
##    while a<=n:
##        if a%k==0:
##            a+=1
##        Sum+=a
##        a+=1
##    return Sum
##a=int(input())
##b=int(input())
##print(FindSum(a,b))
        



##s=str(input())
##s=s.split(' ')
##s=' '.join(reversed(s))
##s=s.replace(' ','.')
##print(str(s))



##a,b=map(int,input().split())
##c=a//2
##d=a-c
##print(b*d)


##def IsSumPossible(b,c):
##    for i in range(len(c)):
##        for j in range(len(c)):
##            if c[i]+c[j]==b:
##                return 1
##    else:
##        return 0
##
##
##a=int(input())
##N=int(input())
##arr=list(map(int,input().split()))
##print(IsSumPossible(N,arr))




##X=int(input())
##c=0
##for i in range(X+1):
##    if (i*2)<=X:
##        c+=i*2
##    else:
##        break
##print(i)



##def numElementsInBetweenInclusive(num1,num2,arr):
##    for i in range(len(arr)):
##        if num1<=arr[i]<=num2:
##            print(arr[i])
##    
##
##num1=int(input())
##num2=int(input())
##arr=list(map(int,input().split()))
##a=numElementsInBetweenInclusive(num1,num2,arr)



##def Cuckoo_sequence(n):
##    if n==1:
##        return 0
##    elif n==2:
##        return 1
##    else:
##        return 1*Cuckoo_sequence(n-1)+2*Cuckoo_sequence(n-2)+3*1
##
##input1=int(input())
##a=Cuckoo_sequence(input1)
##print(a)


##r=c=int(input())
##matrix=[[int(input()) for x in range(r)] for y in range(c)]
##a=[[(matrix[i][j]) for i in range(len(matrix)-1,-1,-1)]for j in range(len(matrix))]
##print(a)
        
  
        
##N=int(input())
##A=list(map(int,input().split()))
##a=[]
##c=0
##for i in range(len(A)):
##    for j in range(len(A)):
##        if (A[i],A[j]) not in a:
##            c+=1
##            a.append((A[i],A[j]))
##print(c)
##print(a)



##N=int(input())
##A=list(map(int,input().split()))
##while sorted(A)!=A:
##    for i in range(len(A)-1):
##        if A[i]>A[i+1]:
##            A[i],A[i+1]=A[i+1],A[i]
##print(A)
##print(A[::-1])


##def Fun(a,b,c):
##    a=b+c
##    b=a+c
##    c=a+b
##    return a,b,c
##
##x=1
##y=2
##print(Fun(x,y,y))



##def digitSumDiff(a,b):
##    res=0
##    c=0
##    for i in range(a,b+1):
##        c=0
##        while i!=0:
##            r=i%10
##            c+=r
##            i=i//10
##        res+=c
##    return res
##        
##
##s=input().split()
##a=int(s[0])
##b=int(s[1])
##print(digitSumDiff(a,b))




##a=[1,2,3,4,5]
##b=[6,7,8,9,10]
##c=0
##for i in range(len(a)):
##    c+=1
##    print(a[i],b[-c])



##for i in range(65,91):
##    print(chr(i))
##    
##for j in range(97,123):
##    print(chr(j))



##N=int(input())
##a=0
##b=1
##print(a,end="")
##print(b,end="")
##for i in range(N-2):
##    ab=65+i
##    c=a+b
##    a=b
##    b=c
##    print(c,end="")
##    for j in range(ab,91):
##        print(chr(j),end="")
##        break
    

##def fibonacci(q):
##    A=[]
##    a=1
##    b=1
##    A.append(a)
##    A.append(b)
##    for i in range(q-2):
##        c=a+b
##        A.append(c)
##        a=b
##        b=c
##    return A
##    
##
##N=input()
##Q=fibonacci(len(N))
##a=[]
##a.append(str(sum(Q)))
##for i in range(len(N)):
##    for j in range(len(Q)):
##        if i==j:
##            a.append(N[i])
##            a.append(str(Q[j]))
##print("".join(a))


##def factorial(x):
##    count=1
##    for i in range(x,0,-1):
##         count*=i
##    return count
##
##
##a=list(map(int,input().split()))
##b=list(map(int,input().split()))
##f=[]
##for i in range(len(a)):
##    for j in range(len(b)):
##        if i==j:
##            c=factorial(a[i])
##            d=factorial(b[j])
##            e=factorial(a[i]-b[j])
##            f.append(c//(d*e))
##g=[]
##g.append(sum(a))
##g.append(sum(b))
##h=factorial(g[0])
##i=factorial(g[1])
##j=factorial(g[0]-g[1])
##f.append(h//(i*j))
##print(f)
##k=[]
##for i in range(2,f[2]):
##    if (f[0]*f[1])%i==0:
##        if f[2]%i==0:
##            k.append(str(((f[0]*f[1])//i)))
##            k.append('/')
##            k.append(str(f[2]//i))
##print("".join(k))




##s="HeyThereIAmGood "
##for i in range(len(s)-1):
##    if s[i].isupper():
##        a=[]
##        if s[i+1].isupper():
##            print(s[i])
##        elif s[i+1].islower():
##            a.append(s[i])
##    else:
##        if s[i].islower():
##            a.append(s[i])
##        if s[i+1].isupper():
##                print("".join(a),"121")
##print("".join(a),"124")

                               
    
##import re          
##s="HeyThereIAmGood"
##a=re.findall('[A-Z][^A-Z]*',s)
##for i in range(len(a)):
##    print(a[i])
##        


##s="HeyThereIAmGood"
##a=list(s)
##x=0
##for i in range(len(a)):
##    if a[i].isupper() and i!=0:
##        print("".join(a[x:i]))
##        x=i
##print("".join(a[x:i+1]))



##def regimen(x):
##    count=0
##    if x<=4:
##        for i in range(1,x):
##            count+=i
##    else:
##        a=x-3
##        for i in range(a,x+1):
##            b=i-1
##            for j in range(1,b):
##                count+=j
##    return count
##        
##
##a=int(input())
##print(regimen(a))



##a1=int(input())
##a2=int(input())
##a1=[int(x) for x in str(a1)]
##a2=[int(y) for y in str(a2)]
##x=[]
##y=[]
##z=[]
##for i in range(len(a1)):
##    for j in range(len(a2)):
##        if i==j:
##            x.append(str(a1[i]+a2[j]))
##            y.append(str(a1[i]-a2[j]))
##            z.append(str(a1[i]*a2[j]))
##            
##print("".join(x),end=" ")
##print("".join(y),end=" ")
##print("".join(z))



##a=int(input())
##b=list(map(int,input().split()))
##count=0
##for i in range(len(b)):
##    if b[i]<0:
##        count+=1
##print(count)



##def add(a):
##    c=0
##    while a!=0:
##        r=a%10
##        c+=r
##        a=a//10
##    return c
##
##a=int(input())
##b=list(map(int,input().split()))
##for i in range(len(b)):
##    print(add(b[i]),end=" ")


##a=int(input())
##if (30<=a<=50):
##    print("Average")
##elif (51<=a<=60):
##    print("Good")
##elif (61<=a<=80):
##    print("Excellent")
##else:
##    print("Outstanding")




##T=int(input())
##for i in range(T):
##    N=int(input())
##    N=[str(x) for x in str(N)]
##    print(len(N))
##    if len(N)%2==0:
##        a=len(N)//2
##        b="".join((N[:a]))
##        c="".join((N[a:]))
##        if b>c:
##            print("magic number")
##        else:
##            print("normal number")
##    else:
##        a=len(N)//2
##        b="".join(N[:a])
##        c="".join(N[-a:])
##        if b>c:
##            print("magic number")
##        else:
##            print("normal number")
        
        
##a=str(input())
##a=[str(x) for x in str(a)]
##c=0
##for i in range(len(a)):
##    a[i]="".join(a[i])
##    if a[i]>0:
##        c+=1
##print(c)



##n=int(input())
##s=bin(n)
##print(s[2:])



##a=int(input())
##b=list(map(int,input().split()))
##print(max(b)+min(b))




##a,b=map(int,input().split())
##n=1
##while n:         
##    c=b*n        
##    if c%a==0:   
##        print(c) 
##        break
##    n+=1




##a=int(input())
##b=int(input())
##c=list(map(int,input().split()))
##d=0
##for i in range(len(c)):
##    d+=c[i]%b
##print(d)




##a=int(input())
##b=int(input())
##c=int(input())
##count=0
##for i in range(1,a+1):
##    if (i%b==0) or (i%c==0):
##        print(i)
##        count+=i
##print(count)



##import math
##def perfectsquare(x):
##    count=0
##    if (x>0):
##        a=int(math.sqrt(x))
##        if (a*a==x):
##            count+=x
##    return count
##
##a=int(input())
##b=int(input())
##c=0
##for i in range(a,b+1):
##    c+=perfectsquare(i)
##print(c)


##def prime(a):
##    if a==1:
##        return 0
##    for i in range(2,(a//2)+1):
##        if a%i==0:
##            return 0
##
##
##a=int(input())
##d=0
##while a!=0:
##    r=a%10
##    a=a//10
##    if prime(r)>1:
##        d+=r
##print(d)



##num=int(input())
##count=0
##for i in range(1,num+1):
##        if i<9 and i%2==0:
##            count+=1
##        else:
##            c=0
##            while i!=0:
##                r=i%10
##                c+=r
##                i=i//10
##            if c%2==0:
##                count+=1
##                
##print(count)




##lst=[1,2,3,4,5]
##a=[]
##for i in range(0,len(lst)-1):
##        if i%2!=0:
##                a.append(lst[i])
##print(a)




##words = ["abc","car","ada","racecar","cool"]
##for i in range(len(words)):
##    print(words[i],words[i][::-1])

    

##a=3628800
##count=d=e=0
##while a!=0:
##    r=a%10
##    count+=1
##    c=r
##    a=a//10
##    if c==0 and count==e+1:
##        e=count
##        d+=1
##print(d)

##num=7
##a=[]
##while num!=0:
##    a.append(str(num%7))
##    num=num//7
##print("".join(a))



##T=int(input())
##for i in range(T):
##    x,y,n=map(int,input().split())
##    count=0
##    while (n!=y):
##        a=x-y
##        n-=a
##        count+=1
##    print(count)




##n,k=map(int,input().split())
##array=list(map(int,input().split()))
##if(n%2==0):
##    for i in range(len(array)-1):
##        if (abs(array[i]-array[i+1])>=k):
##            count+=1
##        else:
##            count=1
##        print(count,end=" ")
##else:
##    count=1
##    for i in range(len(array)-1):
##        if (abs(array[i]-array[i+1])>=k):
##            count+=1
##        else:
##            count=1
##        print(count,end=" ")






##def prime(x):
##    count=2
##    for k in range(2,(x//2)+1):
##        if(x%k==0):
##            count+=1
##    if (count==2):
##        return x
##    else:
##        return 2
##
##def palindrome(y):
##    count=0
##    a=y
##    while (y!=0):
##        r=y%10
##        count=count*10+r
##        y=y//10
##    if (a==count):
##        return count
##    else:
##        return 3
##
##a,b=map(int,input().split())
##if a>b:
##    a,b=b,a
##if a<b:
##    for i in range(a+1,b+1):
##        x=prime(i)
##        y=palindrome(i)
##        if (x==y):
##            print(i)

            

