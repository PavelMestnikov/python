imn="процент"
rod="процента"
mult="процентов"
for num in range(1,501):
    num=str(num)
    if num[len(num)-2] == "1":
        print(num + " " + mult)
    elif num[len(num)-1] == "1":
        print(num+" "+imn)
    elif  num[len(num)-1] == "2" or num[len(num)-1] == "3" or num[len(num)-1] == "4":
        print(num + " " + rod)
    else:
        print (num + " " + mult)
