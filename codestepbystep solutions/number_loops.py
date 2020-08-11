dot1 = 4
num = 1
dot2 = 0
for i in range(5):
    for j in range(5):
        print("." * dot1,num ,"." * dot2,sep="")#sep= is used to remove unwanted space
        break
    dot1 = dot1 - 1
    num = num + 1
    dot2 = dot2 + 1
