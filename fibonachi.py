n= int(input('enter numbr:'))
list=[]
for i in range (n) :
    if i==0 or i == 1 :
        list.append(1)
    else :
        f = list[i - 1] + list[i - 2]
        list.append(f)       
print(list) 
 