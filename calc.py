def do(x,y,z):
    if z=="add":
        return x+y
    elif z=="sub":
        return x-y
    elif z=="mult":
        return x*y
    elif z=="div":
        if y==0:
            print("errrrrrrrrr") 
            return 0
        return x/y
    else:
        print("wut?") 
        return
print("CALCULATOR") 
print("Do math ok!!") 
x=input("1st number")
y=input("2nd number")
z=input("do wut? (add, sub, mult, div)")
print("Answer is: ",do(int(x),int(y),z))