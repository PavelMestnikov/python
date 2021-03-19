time= int(input())
sec= time%60
min= (time//60)%60
hour= (time//3600)%24
day=  time//86400
if day != 0:print(day,"дн",hour,"час",min,"мин",sec,"сек")
elif hour != 0:print(hour,"час",min,"мин",sec,"сек")
elif min != 0:print(min,"мин",sec,"сек")
