w=int(input("enter the weight of watermelon:"))
if(w%2!=0):
    print("No it is odd")
else:
    x=w/2
    if(x%2==0):
        print("Yes brother1 gets",x,"and brother2 gets",x)
    else:
        print("Yes brother1 gets",x-1,"and brother2 gets",x+1)
