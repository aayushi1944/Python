while True:
    print("==========MENU===========")
    ch=int(input("1) decimal to binary \n2) decimal to octal \n3) decimal to hexadecimal \n9)Exit \nEnter your choice:"))

    if ch in(1,2,3):
        n=int(input("Enter decimal number:\n"))
        if ch==1:
            ans=bin(n)
        elif ch==2:
            ans=oct(n)
        else:
            ans=hex(n)
        print("answer:",ans)
    elif ch==9:
        break
    else:
        print("invalid choice...!\n")
