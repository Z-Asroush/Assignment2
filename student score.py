



x=int(input('enter number of student:'))
count=0
score = []
while count <x:
    count=count+1
    y= float(input('enter student score:' ))

    score.append(y)
print(max(score))
print(min(score))
print(sum(score)/x)

