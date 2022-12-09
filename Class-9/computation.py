from readTextFile import person1, person2, cnt
for i in range(0, cnt):
    if (i+1)%2!=0:
        print("person1 : "+person1[i//2])
    else :
        print("person2 : " + person2[i//2])

