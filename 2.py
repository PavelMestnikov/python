def summa(num):
    num=str(num)
    count=0
    for i in range(len(num)):
        count+=int(num[i])
    return count

num= str(input())
while num!="0":
    print(summa(num))
    num= str(input())