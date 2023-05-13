from tyre.tyre import Tyre

class Carrigan(Tyre):
    def __init__(self,array):
        self.arr = array
    
    def needs_service(self):
        count =0
        for i in range(len(self.arr)):
            if self.arr[i] >= 0.9:
                count = count+1
        if(count >= 1):
            return True
        else:
            return False
