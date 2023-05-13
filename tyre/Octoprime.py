from tyre.tyre import Tyre

class Octoprime(Tyre):
    def __init__(self,array):
        self.arr = array
    
    def needs_service(self):
        sum=0
        for i in range(len(self.arr)):
            sum = sum+arr[i]
        if sum >= 3:
            return True
        else:
            return False
