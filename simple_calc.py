while True:
    print("\n\n1=> +")
    print("2=> -")
    print("3=> *")
    print("4=> /")
    print("5=> %")

    ch=int(input("Enter choice[1-5]:"))
    if ch==5:
        break
    
    if ch>=1 and ch <=6:
        n1=int(input("Enter n1:"))
        n2=int(input("Enter n2:"))

        if ch==1:
            print(n1+n2)
        elif ch==2:
            print(n1-n2)
        elif ch==3:
            print(n1*n2)
        elif ch==4:
            print(n1/n2)
        elif ch==5:
            print(n1%n2)
    else:
        print("invalid choice...!")


