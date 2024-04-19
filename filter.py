ages = [5, 12, 17, 18, 24, 32]

above_18=list(filter(lambda x: x>=18, ages))
print(above_18)

#myFun 사용
def myFun(x):
    if x>=18:
        return True
    else:
        return False
    
above_18_2=list(filter(myFun,ages))
print(above_18_2)