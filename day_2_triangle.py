n=int(input("Enter no:"))

# for i in range(n):
#     ch=65
#     for j in range(i):
#         print(chr(ch),end=" ")
#         ch = ch+1
#     print("\n")

for i in range(n):
    ch=65
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(chr(ch),end=" ")
        ch = ch+1
    print()

