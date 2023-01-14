def intsum():
    FinalList=[]
    for i in range(100,201):
        digits =[int(e) for e in str(i)]
        if sum(digits)%2 ==0:
            FinalList.append(i)
        else:
            pass
    print(FinalList)
# intsum()

def reverseint():
    inital = input("Enter the number (positive) : ")
    