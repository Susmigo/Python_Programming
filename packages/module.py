class File():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b

    
    
class Find():
    def even(n):
        if n%2==0:
            print('even')
        else:
            print('odd')
        return 
    

    
class Mod():
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def __add__(self):
        return self.val1+self.val2
    def __mul__(self):
        return self.val1*self.val2