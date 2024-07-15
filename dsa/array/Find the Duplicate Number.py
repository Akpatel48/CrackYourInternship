def dublicate(array):
    dublicat=[]
    o=[]
    for i in array:
        if i in o:
            dublicat.append(i)
        else:
            o.append(i)
    print("dublicate values:",dublicat)

array=[]
size=int(input("enter lanth of array:"))
for i in range(size):
    array.append(input("enter array value:"))
    
dublicate(array)