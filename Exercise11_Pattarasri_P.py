number = int(input(""))
print("Input","Output")
print(number,end="")
for x in range(number):
    print(1*"\t"," " * (number-x-1),"*" * (((x+1)*2)-1))
