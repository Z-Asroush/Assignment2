s=int(input('secend:'))

h=int(s/3600)
b1=int(s%3600)
m=int(b1/60)
s=int(b1%60)

print (h,':',m,':', s)
