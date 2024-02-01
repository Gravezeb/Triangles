print("\n")
print("\n")
print("\t \t \t Triangles ")

name = "seb"
age = 3

#print(f"hi my name is {name}{age}")
print(f"lets print some triangles for  {name}")
print(f"sebas current age is {age} so his triangle looks like this:")
for i in range(1,age+1):
    print(i*"*")
#--------------------------------------
print("\t mirrored") 
for i in range(1,age+1):
    start_index=age-i
    print(" "*start_index,end="" )
    for star in range(i):
        print("*",end="")
    print(" ")    
#---------------------------------------------
print("now centered")
for i in range (1,age+1):
    center_index=age-i
    print(" "*center_index,end="")
    for EOstar in range(i+i-1):
        if EOstar % 2:
            print(" ",end="")
        else:
            print("*",end="")
    print(" ")