b=["hello","you are great"]
bb=0
bbb=" "
print("\x1bc\x1b[47;34m")
while True:
    print(b[bb])
    bb+=1
    bb=bb & 1
    bbb=""
    bbb=input(">")
    if bbb=="":
        break
    f1=open("chatai.txt","a")
    f1.write(bbb+"\n")
    f1.close()
print("by")