def summa(num):
    num=str(num)
    count=0
    for i in range(len(num)):
        count+=int(num[i])
    return count

def count(nums):
    amount = 0
    for num in nums:
        a = summa(num)
        if a % 7 == 0:
            amount += num
    print(amount)
nums= [i**3 for i in range(1, 1001)]
count(nums)
nums= [int(str(nums[i])+"17") for i in range(0, 1000)]
count(nums)
amount = 0
for num in range(1, 1001):
    num= str(num**3)+"17"
    a= summa(num)
    if a%7==0:amount+=int(num)
print(amount)