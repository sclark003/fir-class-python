import numpy as np

class FIR_filter:
    def __init__(self,coefficients):
        self.coefficients = coefficients
        self.buffer = np.zeros(len(self.coefficients))
        self.ptr= len(self.coefficients)-1
        self.numTaps = len(self.coefficients)
        
    def dofilter(self, v):
        result = 0
        self.buffer[self.ptr] = v #store the input value in the buffer
        # 
        result += np.dot(self.buffer[self.ptr : self.numTaps] , self.coefficients[0 : self.numTaps-self.ptr])
        result += np.dot(self.buffer[0 : self.ptr] , self.coefficients[self.numTaps-self.ptr : self.numTaps])
        self.ptr -= 1 # decrement ptr
        
        if (self.ptr < 0):
            self.ptr = self.numTaps - 1
            
        return result