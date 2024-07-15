def dublicate():
    dub=[]
    array=[]
    size=int(input("enter array size:"))
    for i in range(size):
        array.append(input("enter array values:"))
        for i in array:
            if i not in dub:
                dub.append(i)
    return dub
def sort(array):
    no=len(array)
    
    if no>=2:
        for i in range(no):
            for j in range(no-1):
                if int(array[j])<=int(array[j+1]):
                    None
                else:
                    print(array[j],array[j+1]) 
                    array[j],array[j+1]=array[j+1],array[j]
            print(' ')
            print(array)

    
sort(dublicate())
