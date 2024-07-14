print("enter the five sub.. marks")
aco=int(input("enter the mark of aco:"))
ing=int(input("enter the mark of ing:"))
state=int(input("enter the mark of state:"))
sp=int(input("enter the mark of sp:"))
ba=int(input("enter the mark of ba:"))
total=aco+ing+state+sp+ba
avg=total/5
if(aco<=100 and ing<=100 and state<=100 and sp<=100 and ba<=100):
    print("total:",total)
    if(aco>=33 and ing>=33 and state>=33 and sp>=33 and ba>=33):
        print("pass")
        print("avg:",avg,"%")
        if(avg>=91 and avg<=100):
            print("your gread is:A1")
        elif(avg>=81 and avg<91):
            print("your gread is:A2")
        elif(avg>=71 and avg<81):
            print("your gread is:B1")
        elif(avg>=61 and avg<71):
            print("your gread is:B2")
        elif(avg>=51 and avg<61):
            print("your gread is:C1")
        elif(avg>=41 and avg<51):
            print("your gread is:D1")
        else:
            print("your gread is:D2")
    else:
        print("sorry you are fail")
else:
    print("enter the valid marks")