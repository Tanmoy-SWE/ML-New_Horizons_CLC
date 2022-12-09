passwords = ['abcd', 'hello', 'breakpass', 'correctpass']

j = 0
while(j<3):
    passInput  = input("Enter your password : ")
    flag = False
    for i in range(0, len(passwords)):
        if passwords[i] == passInput:
            flag = True
    if flag == False :
        print("You entered wrong password!!")
    else :
        print("You can now play rock paper scissor.")
    j = j + 1
