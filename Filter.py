import sys

# Function types: (1, is addition), (2, subtraction), (3, multiplication)

class Filter:
    def __init__(self, num):
        self.data = []
        self.weight = num

    def compute(self, input):
        return (input + self.weight)
    
    def reverse_compute(self, input):
        return (input - self.weight)
        
    def get_weight(self):
        var = self.weight
        return var
